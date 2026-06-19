"""
state_nav.py — 50-state truck navigation reference center.

Honest scope note: this is a REFERENCE and TRIP-PLANNING tool, not a live
turn-by-turn GPS engine. What this module provides: official truck-route
resource links per state, known regional hazard patterns, and a structured
pre-trip planning workflow you actually use before driving.
"""

STATE_DATA = {
    "Alabama": {"dot_url": "https://www.dot.state.al.us/", "permit_url": "https://www.dot.state.al.us/dsweb/", "notes": "Watch for lower clearance on older rural bridges; Mobile's port corridor has dense truck traffic."},
    "Alaska": {"dot_url": "https://dot.alaska.gov/", "permit_url": "https://dot.alaska.gov/comveh/", "notes": "Extreme weather closures are common; many routes have no practical detour."},
    "Arizona": {"dot_url": "https://azdot.gov/", "permit_url": "https://azdot.gov/motor-vehicles/professional/permits", "notes": "Extreme summer heat affects tire/brake performance on long grades; dust storm zones require specific protocol."},
    "Arkansas": {"dot_url": "https://www.ardot.gov/", "permit_url": "https://www.ardot.gov/divisions/maintenance/permits/", "notes": "River crossings concentrate truck traffic onto a few key bridges — check posted weight limits before routing."},
    "California": {"dot_url": "https://dot.ca.gov/", "permit_url": "https://dot.ca.gov/programs/traffic-operations/permits", "notes": "Mountain grade chain requirements in winter; LA/Long Beach port corridors are heavily congested; strict idling/emissions rules."},
    "Colorado": {"dot_url": "https://www.codot.gov/", "permit_url": "https://www.codot.gov/business/permits", "notes": "Mountain pass chain laws and runaway truck ramps are common — know your brake check points on long descents."},
    "Connecticut": {"dot_url": "https://portal.ct.gov/dot", "permit_url": "https://portal.ct.gov/dot/services/permitting", "notes": "Dense parkway network with truck bans similar to NYC parkways — many scenic routes are passenger-vehicle only."},
    "Delaware": {"dot_url": "https://deldot.gov/", "permit_url": "https://deldot.gov/Business/oversize/index.shtml", "notes": "I-95 corridor tolling and congestion near Wilmington; small state but high through-traffic density."},
    "Florida": {"dot_url": "https://www.fdot.gov/", "permit_url": "https://www.fdot.gov/agencyresources/trucking/", "notes": "Hurricane season can close major corridors with little notice; toll-by-plate systems are widespread."},
    "Georgia": {"dot_url": "https://www.dot.ga.gov/", "permit_url": "https://www.dot.ga.gov/GDOT/Pages/PermitsOnline.aspx", "notes": "Atlanta's I-285/I-75/I-85 interchange complex is a major routing/congestion point for through-trucks."},
    "Hawaii": {"dot_url": "https://hidot.hawaii.gov/", "permit_url": "https://hidot.hawaii.gov/highways/doing-business/permits/", "notes": "Limited highway network per island; interisland freight typically requires barge/ferry coordination."},
    "Idaho": {"dot_url": "https://itd.idaho.gov/", "permit_url": "https://itd.idaho.gov/itd-services/?target=permits", "notes": "Mountain grades and winter chain requirements on key passes; long distances between services."},
    "Illinois": {"dot_url": "https://idot.illinois.gov/", "permit_url": "https://idot.illinois.gov/transportation-system/network-overview/permits", "notes": "Chicago's expressway interchanges and tollway system are a major congestion and routing factor."},
    "Indiana": {"dot_url": "https://www.in.gov/indot/", "permit_url": "https://www.in.gov/indot/business-center/permits/", "notes": "Major east-west freight corridor (I-70/I-80); Indianapolis beltway congestion at peak hours."},
    "Iowa": {"dot_url": "https://iowadot.gov/", "permit_url": "https://iowadot.gov/mvd/oversize-overweight", "notes": "Rural two-lane stretches with limited shoulder — extra caution passing/being passed."},
    "Kansas": {"dot_url": "https://www.ksdot.org/", "permit_url": "https://www.ksdot.org/burTransPlan/permits", "notes": "High-wind corridors common in open plains — affects high-profile trailers especially."},
    "Kentucky": {"dot_url": "https://transportation.ky.gov/", "permit_url": "https://transportation.ky.gov/Motor-Carriers/Pages/Permits.aspx", "notes": "Mountainous eastern routes have steep grades and tight curves; river crossings concentrate traffic."},
    "Louisiana": {"dot_url": "https://wwwsp.dotd.la.gov/", "permit_url": "https://wwwsp.dotd.la.gov/Inside_LaDOTD/Divisions/Operations/Permits/Pages/default.aspx", "notes": "Hurricane evacuation routing can override normal truck routes; bayou-region bridges have specific weight limits."},
    "Maine": {"dot_url": "https://www.maine.gov/mdot/", "permit_url": "https://www.maine.gov/mdot/maintenance/oversize/", "notes": "Winter weather severity is a major planning factor; rural coverage gaps for services."},
    "Maryland": {"dot_url": "https://www.mdot.maryland.gov/", "permit_url": "https://www.mdot.maryland.gov/newMDOT/Permits/", "notes": "Baltimore/DC beltway congestion; Chesapeake Bay Bridge has truck-specific restrictions during high wind."},
    "Massachusetts": {"dot_url": "https://www.mass.gov/orgs/massachusetts-department-of-transportation", "permit_url": "https://www.mass.gov/how-to/apply-for-an-oversizeoverweight-permit", "notes": "Boston's tunnel system has hazmat and height restrictions similar in spirit to NYC tunnels."},
    "Michigan": {"dot_url": "https://www.michigan.gov/mdot", "permit_url": "https://www.michigan.gov/mdot/programs/permits", "notes": "Heavy winter lake-effect snow on western routes; Detroit's international border crossings add inspection time."},
    "Minnesota": {"dot_url": "https://www.dot.state.mn.us/", "permit_url": "https://www.dot.state.mn.us/cvo/permits/", "notes": "Extreme winter cold affects air brake and diesel performance — cold-weather operation protocol matters here."},
    "Mississippi": {"dot_url": "https://mdot.ms.gov/", "permit_url": "https://mdot.ms.gov/portal/permits", "notes": "River crossings and flood-prone lowland routes — check seasonal closures."},
    "Missouri": {"dot_url": "https://www.modot.org/", "permit_url": "https://www.modot.org/motor-carrier-services", "notes": "St. Louis and Kansas City interchange complexes are major through-freight chokepoints."},
    "Montana": {"dot_url": "https://www.mdt.mt.gov/", "permit_url": "https://www.mdt.mt.gov/business/permits/", "notes": "Very long distances between services; mountain passes require winter chain readiness."},
    "Nebraska": {"dot_url": "https://dot.nebraska.gov/", "permit_url": "https://dot.nebraska.gov/business-center/trucking/permits/", "notes": "High-wind open corridors; I-80 is the dominant east-west freight spine."},
    "Nevada": {"dot_url": "https://www.dot.nv.gov/", "permit_url": "https://www.dot.nv.gov/doing-business/permits", "notes": "Extreme summer desert heat; long stretches with limited services between Las Vegas and Reno."},
    "New Hampshire": {"dot_url": "https://www.nh.gov/dot/", "permit_url": "https://www.nh.gov/dot/org/operations/highwaydesign/permits/", "notes": "Mountain/notch routes have grade and winter considerations similar to Vermont and Maine."},
    "New Jersey": {"dot_url": "https://www.nj.gov/transportation/", "permit_url": "https://www.nj.gov/transportation/business/permits/", "notes": "Extremely dense, NYC-adjacent congestion; many NJ parkways also restrict trucks, mirroring NYC parkway bans."},
    "New Mexico": {"dot_url": "https://dot.nm.gov/", "permit_url": "https://dot.nm.gov/business/permits/", "notes": "High desert elevation changes affect engine/brake performance; long service gaps in rural stretches."},
    "New York (Outside NYC)": {"dot_url": "https://www.dot.ny.gov/", "permit_url": "https://www.dot.ny.gov/divisions/operating/osc/permits", "notes": "Upstate winter severity is significant; thruway tolling and weigh stations are frequent — see the NYC modules for the five boroughs."},
    "North Carolina": {"dot_url": "https://www.ncdot.gov/", "permit_url": "https://www.ncdot.gov/business/permits/Pages/default.aspx", "notes": "Coastal hurricane evacuation routing; mountain grades in the western part of the state."},
    "North Dakota": {"dot_url": "https://www.dot.nd.gov/", "permit_url": "https://www.dot.nd.gov/divisions/maintenance/permits.htm", "notes": "Severe winter conditions and high-wind exposure on open plains routes."},
    "Ohio": {"dot_url": "https://www.transportation.ohio.gov/", "permit_url": "https://www.transportation.ohio.gov/working/permits", "notes": "Major east-west and north-south freight crossroads; turnpike tolling and weigh stations are frequent."},
    "Oklahoma": {"dot_url": "https://oklahoma.gov/odot.html", "permit_url": "https://oklahoma.gov/odot/programs-and-services/permits.html", "notes": "Severe weather (tornado risk) can require rapid route changes; turnpike network is extensive."},
    "Oregon": {"dot_url": "https://www.oregon.gov/odot/", "permit_url": "https://www.oregon.gov/odot/Forms/Pages/Permits.aspx", "notes": "Oregon requires weight-mile tax registration for many commercial vehicles — a compliance step beyond routing."},
    "Pennsylvania": {"dot_url": "https://www.penndot.pa.gov/", "permit_url": "https://www.penndot.pa.gov/RegionalOffices/permits/Pages/default.aspx", "notes": "Mountainous central PA routes plus PA Turnpike tunnels — both grade and clearance factors apply."},
    "Rhode Island": {"dot_url": "https://www.dot.ri.gov/", "permit_url": "https://www.dot.ri.gov/business/permits.php", "notes": "Smallest state but dense Providence-area congestion; bridge-heavy geography."},
    "South Carolina": {"dot_url": "https://www.scdot.org/", "permit_url": "https://www.scdot.org/business/permits.aspx", "notes": "Hurricane evacuation routing on coastal corridors; port of Charleston traffic concentration."},
    "South Dakota": {"dot_url": "https://dot.sd.gov/", "permit_url": "https://dot.sd.gov/doing-business/permits", "notes": "Long rural distances with limited services; I-90 is the dominant corridor."},
    "Tennessee": {"dot_url": "https://www.tn.gov/tdot.html", "permit_url": "https://www.tn.gov/tdot/driver-and-vehicle-permits.html", "notes": "Mountain grades near the eastern border; Nashville/Memphis are major freight hub congestion points."},
    "Texas": {"dot_url": "https://www.txdot.gov/", "permit_url": "https://www.txdot.gov/business/permits.html", "notes": "Massive geographic range — desert heat in the west, hurricane risk on the Gulf coast, dense urban congestion in DFW/Houston."},
    "Utah": {"dot_url": "https://www.udot.utah.gov/", "permit_url": "https://www.udot.utah.gov/main/f?p=100:pg:0:::1:T,V:1412", "notes": "Mountain canyon routes require winter chain readiness; elevation changes affect braking on long descents."},
    "Vermont": {"dot_url": "https://vtrans.vermont.gov/", "permit_url": "https://vtrans.vermont.gov/permits", "notes": "Rural mountain routes with limited truck-route infrastructure; winter severity is significant."},
    "Virginia": {"dot_url": "https://www.virginiadot.org/", "permit_url": "https://www.virginiadot.org/business/trucking_permits.asp", "notes": "DC-adjacent congestion in Northern Virginia; Hampton Roads tunnel network has hazmat and height restrictions."},
    "Washington": {"dot_url": "https://wsdot.wa.gov/", "permit_url": "https://wsdot.wa.gov/business-wsdot/permits", "notes": "Mountain pass closures in winter; Seattle-area congestion and ferry-dependent routing in some corridors."},
    "West Virginia": {"dot_url": "https://transportation.wv.gov/", "permit_url": "https://transportation.wv.gov/highways/trafficsafety/Pages/Permits.aspx", "notes": "Mountainous statewide terrain — grade management is a constant factor, not an occasional one."},
    "Wisconsin": {"dot_url": "https://wisconsindot.gov/", "permit_url": "https://wisconsindot.gov/Pages/doing-bus/freight-carriers/permits/default.aspx", "notes": "Lake-effect snow on eastern routes; dairy/agricultural freight has seasonal volume spikes."},
    "Wyoming": {"dot_url": "https://www.dot.state.wy.us/", "permit_url": "https://www.dot.state.wy.us/home/permitting_registration.html", "notes": "Severe high-wind corridors (especially I-80) regularly close to high-profile trucks — check wind advisories specifically."},
}

PRETRIP_WORKFLOW = [
    {"step": 1, "title": "Enter real vehicle specs into your truck GPS",
     "detail": "Height, weight, length, axle count, and hazmat status — every time, especially after swapping trailers or changing load weight."},
    {"step": 2, "title": "Cross-check the destination state's official truck route resource",
     "detail": "Use the official DOT link for the state(s) you're routing through, not just your GPS app's default suggestion."},
    {"step": 3, "title": "Check bridge, tunnel, and parkway/expressway restrictions specifically",
     "detail": "Route-level approval doesn't guarantee every bridge or tunnel segment is clear — verify known restriction points along the path."},
    {"step": 4, "title": "Check weather and seasonal advisories for the full route",
     "detail": "Mountain chain laws, high-wind advisories, hurricane evacuation routing, and lake-effect snow all override normal routing assumptions."},
    {"step": 5, "title": "Plan your last-mile delivery approach before you're in it",
     "detail": "Identify the legal final-block approach, parking/loading zone, and a backup plan before committing the vehicle to a tight area."},
    {"step": 6, "title": "Confirm hours-of-service math for the full trip",
     "detail": "Build in your 30-minute break and any sleeper-berth split before departure, not as an improvisation mid-route."},
    {"step": 7, "title": "Identify a bailout plan",
     "detail": "Know at least one safe pull-off or reroute option before entering any segment with low clearance, narrow streets, or heavy congestion."},
]

NATIONAL_HAZARD_PATTERNS = [
    {"region": "Northeast urban corridors (NYC, Boston, Philadelphia, DC)",
     "pattern": "Dense parkway truck bans, low historic bridges, tunnel hazmat restrictions, and heavy congestion pricing/tolling zones."},
    {"region": "Mountain West (CO, UT, WY, MT, ID)",
     "pattern": "Steep grades, mandatory chain laws in winter, high-wind corridor closures, and long distances between services."},
    {"region": "Gulf Coast & Southeast coastal (FL, LA, TX coast, SC, NC)",
     "pattern": "Hurricane season evacuation routing that overrides normal truck routes with little notice."},
    {"region": "Upper Midwest & Northern Plains (MN, ND, SD, WI, MI)",
     "pattern": "Severe winter conditions, lake-effect snow, and extreme cold affecting air brake and diesel performance."},
    {"region": "Desert Southwest (AZ, NV, NM, west TX)",
     "pattern": "Extreme summer heat affecting tire and brake performance on long grades, plus dust storm protocol."},
]


def get_state_list() -> list:
    return sorted(STATE_DATA.keys())


def get_state_info(state: str) -> dict:
    return STATE_DATA.get(state, {})
