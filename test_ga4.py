import os
import json
from google.oauth2.credentials import Credentials
from google.analytics.admin import AnalyticsAdminServiceClient
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    RunReportRequest,
)

def get_credentials():
    with open('user_credentials.json', 'r') as f:
        info = json.load(f)
    return Credentials.from_authorized_user_info(info)

def main():
    creds = get_credentials()
    
    # 1. Initialize Admin client to list properties
    print("Fetching GA4 Accounts and Properties...")
    admin_client = AnalyticsAdminServiceClient(credentials=creds)
    
    accounts = admin_client.list_accounts()
    property_id = None
    
    for account in accounts:
        print(f"Account: {account.display_name} (ID: {account.name})")
        # List properties for this account
        properties = admin_client.list_properties(filter=f"parent:{account.name}")
        for prop in properties:
            print(f"  - Property: {prop.display_name} (ID: {prop.name})")
            # We just grab the first property we find
            if not property_id:
                property_id = prop.name.split('/')[1]
                
    if not property_id:
        print("No GA4 Properties found.")
        return

    print(f"\nFound Property ID: {property_id}")
    print("Testing GA4 Data API...")
    
    # 2. Initialize Data client to run a simple report
    data_client = BetaAnalyticsDataClient(credentials=creds)
    
    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name="city")],
        metrics=[Metric(name="activeUsers")],
        date_ranges=[DateRange(start_date="7daysAgo", end_date="today")],
    )
    
    try:
        response = data_client.run_report(request)
        print("\n=== GA4 Report: Active Users by City (Last 7 Days) ===")
        print("City\t\tActive Users")
        print("-" * 40)
        
        has_data = False
        for row in response.rows:
            has_data = True
            print(f"{row.dimension_values[0].value}\t\t{row.metric_values[0].value}")
            
        if not has_data:
            print("No data found for the last 7 days.")
    except Exception as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    main()
