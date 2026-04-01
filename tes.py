import requests
import sys

def send_password_reset_request():
    # URL endpoint
    url = "https://hackerone.com/users/password"
    
    # Headers dari request
    headers = {
        "Host": "hackerone.com",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://hackerone.com/users/password/new",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://hackerone.com",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Priority": "u=0, i",
        "Te": "trailers"
    }
    
    # Cookies
    cookies = {
        "h1_device_id": "3806a30a-2dbc-4ccb-a6aa-0bf3581fed43",
        "__Host-session": "dC8rTHJPeEkxb1JWcXlCOFFIT0cxckkwR0xWVjA5dlc0bzZGTlZ2bjZRR0dKNjVRQUpub29BNVRCVlR2ZnQxYkp3NHZjR1NiaUJ2TlcrUlZCbE5ERlZDNVJHSi9tT253SlRhTkVYQ3BscDlsRWd3YzZGOXF0MFBidHNiSm0xMkNlcFJrQU1PcmdZRDUvNWFieHlDSENtanp3SXdSNnFqcGtwRkFOU0hYd2lVMkp3Qmw3eEtTYnJ4eFZ2d1JlZCtJbFJ6bGFLTE8wTVF2VCtjVWwxdGkwRFhEV2tGdFFXdW0xMlpPbk5kT01IdWlZaGtaWWYvbUNDSUl2L2Y3bmJmM2tFNnE0cFRzdWR4VnE0bWRWcUx6VlVzRmRPQnhEdnRGSng3TVk0c296NWo5V1hScnh4bkZxdTc0OVNia2xiRDcrT1pPV2NzYm85cGMwU3JYMDhiTlBRPT0tLXJhOXpXUDdTdzRBaDRLdzJPc1oxcVE9PQ%3D%3D--cc72b69ea0162c87ba7152e00ae56ca38579834b",
        "_dd_s": "rum=0&expire=1775080589868",
        "AMP_b7cba2c14c": "JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjI2ZTM1MzQ5Zi02NTRlLTRhMTAtYTc1Ny0zMDk5NGExMmE1MDUlMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzc1MDc3OTE1MzMyJTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTc3NTA3OTYwODcwMyUyQyUyMmxhc3RFdmVudElkJTIyJTNBOSUyQyUyMnBhZ2VDb3VudGVyJTIyJTNBMCUyQyUyMmNvb2tpZURvbWFpbiUyMiUzQSUyMi5oYWNrZXJvbmUuY29tJTIyJTdE",
        "__stripe_mid": "3585e05a-4cd8-429e-9c55-51496110c9392dbedd",
        "__stripe_sid": "5dc06432-3e7e-4aa2-bb06-1deb02c0b251a3f341",
        "cf_clearance": "ExBCcd_w1I36MKrUGm50_BN7BynBqsFTojYB.qJw9zY-1775079532-1.2.1.1-HzsMOFrcTf6BQ62KJkzOrotAouiCrn7QzyB7CuwKQkywzATuJ0vOmJ6Mg3PtqqC4WpUXQKdqieCWDBHPjz1yod0oQfHag4eraYTBee1fEkuS3S90aHlDMq0SblB7Iq94E1yzXJhwhmgbGIHGs3twZ3.Nqv3KoHpJ9xZs3ILC9ruwDt17.Jth9vRr7c1PdoIBKpUpCkQlI16tM7wj4Qil2FFBb9lRpX6ueGCaarTMqTM",
        "AMP_MKTG_b7cba2c14c": "JTdCJTdE",
        "cf_chl_rc_ni": "2"
    }
    
    # Data body (form-urlencoded)
    data = {
        "authenticity_token": "l1C5VslE_s9sYxp6ZBUnXcfDl2YlTrUYmgNUDFB7iFpZm2vPPgCbW-MOoJCuDeujYQtR1yvSwSVb7FQpsDgGZg",
        "user[email]": "bauq7uuh7u7@proton.me"
    }
    
    try:
        # Kirim request POST
        print("=" * 50)
        print("Mengirim request ke:", url)
        print("=" * 50)
        
        response = requests.post(
            url,
            headers=headers,
            cookies=cookies,
            data=data,
            allow_redirects=False  # Tidak follow redirect untuk melihat response asli
        )
        
        # Tampilkan hasil
        print(f"\nStatus Code: {response.status_code}")
        print(f"Status Text: {response.reason}")
        print("\n" + "=" * 50)
        print("Response Body:")
        print("=" * 50)
        
        # Tampilkan body response
        try:
            # Coba decode dengan UTF-8
            print(response.text)
        except:
            # Jika gagal, tampilkan raw content
            print(response.content)
        
        print("\n" + "=" * 50)
        print("Response Headers:")
        print("=" * 50)
        for key, value in response.headers.items():
            print(f"{key}: {value}")
            
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    print("\n=== Simple HTTP Request Tool ===\n")
    
    # Tampilkan informasi request yang akan dikirim
    print("Request Details:")
    print("-" * 40)
    print("Method: POST")
    print("URL: https://hackerone.com/users/password")
    print("Content-Type: application/x-www-form-urlencoded")
    print("Data: user[email]=bauq7uuh7u7@proton.me")
    print("\n")
    
    send_password_reset_request()

if __name__ == "__main__":
    main()
