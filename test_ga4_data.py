from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    RunReportRequest,
)
import os

def sample_run_report(property_id="535625144"):
    """Runs a simple report on a Google Analytics 4 property."""
    # Using the credentials defined in GOOGLE_APPLICATION_CREDENTIALS
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "user_credentials.json"
    os.environ["GOOGLE_CLOUD_PROJECT"] = "ga4-mcp-v2-project"

    client = BetaAnalyticsDataClient()

    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name="city")],
        metrics=[Metric(name="activeUsers")],
        date_ranges=[DateRange(start_date="7daysAgo", end_date="today")],
    )
    
    print("Fetching report...")
    response = client.run_report(request)

    print("Report results:")
    for row in response.rows:
        print(row.dimension_values[0].value, row.metric_values[0].value)

if __name__ == "__main__":
    sample_run_report()
