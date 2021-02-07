# http://www.radiocity.si/radiokarantena/

import os.path, random, requests, time

base_url = 'http://www.radiocity.si/karantena/mp3/'
number_of_files = 52
wait_between_requests_min = 2
wait_between_requests_max = 5
directory = 'tmp/'

if not os.path.exists(directory):
    os.makedirs(directory)

print('Starting download...')

for i in range (1, number_of_files):
    if i < 10:
        file = "0" + `i`
    else:
        file = `i`
    url = base_url + file + ".mp3"
    print("Downloading " + url)

    r = requests.get(url)

    file_name = "Radio Karantena - Epizoda " + `i` + ".mp3"
    file = os.path.join(directory, file_name)

    with open(file,'wb') as output_file:
        output_file.write(r.content)

    print("Done")

    # Wait between requests to not flood the server.
    wait_time = random.randint(wait_between_requests_min, wait_between_requests_max)
    print("Waiting between next request for " + `wait_time` + " seconds.")
    time.sleep(wait_time)

print("Download complete.")
