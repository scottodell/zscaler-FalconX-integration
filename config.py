# CrowdStrike - Zscaler Intel Bridge Configuration File
# Enter values prior to first launch
# Confirm that your Zscaler URL Categories contains a User-Defined category named 'CrowdStrike Malicious URLs - High'
proxy = None
logging_level = 'DEBUG'

# CrowdStrike configurations
cs_clientID = "0f3bd757c99c4b048a6958eb0098b36a"
cs_secret = "9zsLQI8NpD5CT2RO3Xbdm0GK61Aqv7njir4FBhMS"
cs_base_url = "https://api.crowdstrike.com"

# ZScaler configurations
zs_hostname = 'https://admin.zscalertwo.net'
cs_category_name = 'CrowdStrike Malicious URLs - High'
zs_username = 'crowdstrike@diversey.corp'
zs_password = 'y2sr2v3D!'
zs_apiKey = ''
zs_max_calls_hourly = 39000  # Maximum URL Look Up requests per hour; Default = 39000
zs_max_payload_size = 10000  # Maximum URLs to POST to Zscaler per request; Default = 10000

