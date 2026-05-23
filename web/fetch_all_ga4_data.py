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
    OrderBy,
)

def get_credentials():
    with open('user_credentials.json', 'r') as f:
        info = json.load(f)
    return Credentials.from_authorized_user_info(info)

def main():
    creds = get_credentials()
    
    property_id = "535625144"
    print(f"\n=== 開始抓取從建立至今的 GA4 流量資料 (資源 ID: {property_id}) ===")
    
    # 2. Initialize Data client to run report
    data_client = BetaAnalyticsDataClient(credentials=creds)
    
    # 設定報表請求 (抓取歷史至今的數據，假設從 2023-01-01 迄今)
    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name="yearMonth")],
        metrics=[
            Metric(name="activeUsers"), 
            Metric(name="screenPageViews"),
            Metric(name="eventCount")
        ],
        date_ranges=[DateRange(start_date="2023-01-01", end_date="today")],
        order_bys=[OrderBy(dimension=OrderBy.DimensionOrderBy(dimension_name="yearMonth"))]
    )
    
    try:
        response = data_client.run_report(request)
        print("\n月份\t\t活躍使用者\t瀏覽量\t\t事件數")
        print("-" * 55)
        
        has_data = False
        total_users = 0
        total_views = 0
        total_events = 0

        for row in response.rows:
            has_data = True
            month = row.dimension_values[0].value
            users = int(row.metric_values[0].value)
            views = int(row.metric_values[1].value)
            events = int(row.metric_values[2].value)
            
            total_users += users
            total_views += views
            total_events += events
            
            print(f"{month[:4]}-{month[4:]}\t{users}\t\t{views}\t\t{events}")
            
        if not has_data:
            print("目前沒有任何流量資料。")
        else:
            print("-" * 55)
            print(f"總計\t\t{total_users}\t\t{total_views}\t\t{total_events}")
            
    except Exception as e:
        print(f"抓取資料時發生錯誤: {e}")

if __name__ == "__main__":
    main()
