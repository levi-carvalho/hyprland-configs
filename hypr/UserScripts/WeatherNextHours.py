from pyquery import PyQuery
from datetime import datetime

def get_next_hours():
    location_id = "11004ae19a644c9d9f05eeb5fe048a760b1537fa239c30bf0e566eac2a7652bc" # TODO

    url = "https://weather.com/en-PH/weather/hourbyhour/l/" + location_id

    html_data = PyQuery(url=url)

    proxima = []
    for i in range(10):
        proxima.append(html_data("div[class='DetailsSummary--DetailsSummary--1DqhO DetailsSummary--hourlyDetailsSummary--2xM-L']").eq(i).text())
        
    

    headers = ["", "", "", ""] # horario, temperatura, % chuva, vento
    col_widths = [5, 7, 4, 11]


    header_row = ""
    for header, width in zip(headers, col_widths):
        header_row += f"{header:^{width}}"
    print(header_row)
    
    text = f"  <span size='70%'>{header_row}</span>\t" +'\n'
    
    # print(html_data("div[class='DetailsSummary--DetailsSummary--1DqhO DetailsSummary--hourlyDetailsSummary--2xM-L']").eq(3).text())
    for hora in proxima:
        print(hora)
        partes = hora.split('\n')
        
        hora_str = partes[0]
        temperatura_str = partes[3]
        precipitacao_str = partes[5]
        
        vento_partes = partes[-1].split(' ')
        vento_direcao = vento_partes[0]
        vento_forca = "".join(vento_partes[1:])
        
        vento_str = f"{vento_direcao.ljust(4, ' ')}{vento_forca}"
        
        text += f"  <span size='70%'>{hora_str:<{5}}  {temperatura_str:<{5}}{precipitacao_str:<{4}} {vento_str:<{1}}</span>\t\n"

    agora = datetime.now()
    agora = agora.strftime("%H:%M")
    
    return text + "\n" + f"<span size='30%'> l.t.u.:{agora}</span>"

print(get_next_hours())