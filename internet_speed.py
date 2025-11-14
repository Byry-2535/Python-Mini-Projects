import speedtest

def perform_speed_test():
    try:
        st = speedtest.Speedtest()
        print('Please wait...')
        st.get_best_server()
        download_speed = st.download() / 1_000_000
        upload_speed = st.upload() / 1_000_000
        ping = st.results.ping
        return download_speed, upload_speed, ping
    except speedtest.SpeedtestException:
        print('Error 405')
        return None, None, None
    
download, upload, ping = perform_speed_test()
if download is not None and upload is not None and ping is not None:
    print(f'\nDownload : {download:.2f} Mbps')
    print(f'Upload   : {upload:.2f} Mbps')
    print(f'Ping     : {ping:.2f}ms')