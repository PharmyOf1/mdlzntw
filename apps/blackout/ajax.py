from apps.blackout.model import USER_PROFILE_CURRENT_SECTOR_TYPES

INDUSTRY_DICT = {
    4: range(14,36),
    5: range(36,58),
    6: range(58,80),
    7: range(80,102),
    8: range(102,124),
    10: range(124,146)  # This is the only true equivalence that you passed to me
}

@csrf_exempt
def get_sectors(request):
    response = []
    industry_id = int(request.POST['industry_id'])

    # With the sector_id you know wich sector the user has selected
    # You should generate the list based in your needs
    data = []
    if industry_id:
        sectors = INDUSTRY_DICT[industry_id]  # This return a list of ID's of sectors
        # Then make loop over all sectors
        for sector_id in sectors:  
            # To get the sector name you should use another dict
            # I think you already have it in USER_PROFILE_CURRENT_SECTOR_TYPES
            # Remember to import it (check above)
            sector_name =  USER_PROFILE_CURRENT_SECTOR_TYPES[sector_id]
            # We append the id and the name to replace options in the HTML
            data.append({'id':sector_id, 'name':sector_name})  

        response = { 'item_list':data }  # We send back the list
        return HttpResponse(simplejson.dumps(response))

    # If we get any error, or cannot get the sector, we send an empty response
    response = {}
    return HttpResponse(simplejson.dumps(response))