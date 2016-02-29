
#pull this off your google sheet
sheet_id = '125NM05dqHKy3-97GkieVwn4V5Iy0Vj-w7erh9tAJxlA'

#do new entries appear immediately on the site
#or do they need to be approved first?
require_approval = False


#what do you want the fields to be called?
#the cannonical names are keys, the names you want to display are values
#don't remove any keys, things will crash
fieldnames = {'Name':'Name',
        'Description':'Description',
        'Category':'Category',
        'Address1':'Address line 1',
        'Address2':'Address line 2',
        'City':'City',
        'State':'State',
        'Zip':'Zipcode',
        'Phone':'Phone number',
        'Website':'Website',
        'Email':'Email Address'
        }

#what categories are allowed? Put in as many as you want but
#they'll display in a menu so if you do tons it'll look bad
#the first item will be the default
categories = ['Other', 'Stuff', 'Things']