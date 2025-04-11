from nekogitlabwrapper import gitlab

def test_cli():
    gitlabcli = gitlab.GitlabCli(url="http",private_token="",ssl_verify=False)
    gitlabcli.__dir__()
    assert gitlabcli._base_url=="http"
# def test_haversine():
#     # Amsterdam to Berlin
#     assert myfunctions.haversine(
#         4.895168, 52.370216, 13.404954, 52.520008
#     ) == 576.6625818456291