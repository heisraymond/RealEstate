import requests

response = requests.get("https://www.realestate.com.au/buy/property-house-land-acreage-rural-size-4000-in-bundaberg+-+greater+region,+qld%3b+sunshine+coast,+qld%3b+sunshine+coast,+hinterland+-+region,+qld%3b+noosa,+qld%3b+gympie+-+greater+region,+qld%3b+caboolture,+qld+4510%3b+brisbane+-+greater+region,+qld%3b+ipswich+-+greater+region,+qld%3b+toowoomba+-+greater+region,+qld%3b+gatton,+qld+4343%3b+beaudesert,+qld+4285%3b+tamborine,+qld+4270%3b+gleneagle,+qld+4285%3b+gold+coast,+qld%3b+tweed+shire,+nsw%3b+tweed+heads,+nsw+2485%3b+coffs+harbour+-+greater+region,+nsw/list-3?misc=ex-under-contract")

print(response.status_code)