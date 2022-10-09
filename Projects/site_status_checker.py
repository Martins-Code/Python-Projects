import urllib.request as urlb


def main(url):
    print("Checking Connectivity")

    response = urlb.urlopen(url)
    print("Connected to", url, "Successfully")
    print("The Response code was : ", response.getcode())


url_input = input("Enter URL: ")

main(url_input)
