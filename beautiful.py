from bs4 import BeautifulSoup

html = """
<table class="table table-hover dataTable no-footer generic-table compact" cellspacing="0" border="0" id="gvSummar" style="width:100%;border-collapse:collapse;" aria-describedby="gvSummar_info">
		<thead>
			<tr><th class="datesp sorting" scope="col" tabindex="0" aria-controls="gvSummar" rowspan="1" colspan="1" aria-label="Data: activate to sort column ascending" style="width: 59.4531px;">Data</th><th scope="col" class="sorting" tabindex="0" aria-controls="gvSummar" rowspan="1" colspan="1" aria-label="Piata: activate to sort column ascending" style="width: 35.3594px;">Piata</th><th class="text-right numericsp sorting" scope="col" tabindex="0" aria-controls="gvSummar" rowspan="1" colspan="1" aria-label="Tranzactii: activate to sort column ascending" style="width: 64.0781px;">Tranzactii</th><th class="text-right numericsp sorting" scope="col" tabindex="0" aria-controls="gvSummar" rowspan="1" colspan="1" aria-label="Volum: activate to sort column ascending" style="width: 51.1094px;">Volum</th><th class="text-right numericsp sorting" scope="col" tabindex="0" aria-controls="gvSummar" rowspan="1" colspan="1" aria-label="Valoare: activate to sort column ascending" style="width: 79.875px;">Valoare</th><th class="text-right numericsp sorting" scope="col" tabindex="0" aria-controls="gvSummar" rowspan="1" colspan="1" aria-label="Pret deschidere: activate to sort column ascending" style="width: 101.922px;">Pret deschidere</th><th class="text-right numericsp sorting" scope="col" tabindex="0" aria-controls="gvSummar" rowspan="1" colspan="1" aria-label="Pret minim: activate to sort column ascending" style="width: 71.9062px;">Pret minim</th><th class="text-right numericsp sorting" scope="col" tabindex="0" aria-controls="gvSummar" rowspan="1" colspan="1" aria-label="Pret maxim: activate to sort column ascending" style="width: 75px;">Pret maxim</th><th class="text-right numericsp sorting" scope="col" tabindex="0" aria-controls="gvSummar" rowspan="1" colspan="1" aria-label="Pret mediu: activate to sort column ascending" style="width: 71.9688px;">Pret mediu</th><th class="text-right numericsp sorting" scope="col" tabindex="0" aria-controls="gvSummar" rowspan="1" colspan="1" aria-label="Pret inchidere: activate to sort column ascending" style="width: 90.8438px;">Pret inchidere</th><th class="text-right sorting" scope="col" tabindex="0" aria-controls="gvSummar" rowspan="1" colspan="1" aria-label="Var. (%): activate to sort column ascending" style="width: 52.4844px;">Var. (%)</th></tr>
		</thead><tbody>
			
		<tr class="odd">
				<td align="left">25.01.2024</td><td align="left">REGS</td><td align="right">1.328</td><td align="right">528.764</td><td align="right">12.662.165,40</td><td align="right">24,2000</td><td align="right">23,8000</td><td align="right">24,3800</td><td align="right">23,9400</td><td align="right">23,8200</td><td class="numericspvar negative" align="right">-1,5700<i class="caret caret-small"></i></td>
			</tr><tr class="even">
				<td align="left">23.01.2024</td><td align="left">REGS</td><td align="right">1.274</td><td align="right">617.781</td><td align="right">15.015.525,96</td><td align="right">24,5800</td><td align="right">24,0200</td><td align="right">24,6000</td><td align="right">24,3000</td><td align="right">24,2000</td><td class="numericspvar negative" align="right">-1,6300<i class="caret caret-small"></i></td>
			</tr><tr class="odd">
				<td align="left">22.01.2024</td><td align="left">REGS</td><td align="right">810</td><td align="right">327.456</td><td align="right">8.142.141,30</td><td align="right">24,9000</td><td align="right">24,6000</td><td align="right">25,0000</td><td align="right">24,8600</td><td align="right">24,6000</td><td class="numericspvar negative" align="right">-1,0500<i class="caret caret-small"></i></td>
			</tr><tr class="even">
				<td align="left">19.01.2024</td><td align="left">REGS</td><td align="right">429</td><td align="right">223.974</td><td align="right">5.568.413,16</td><td align="right">24,8600</td><td align="right">24,7600</td><td align="right">24,9000</td><td align="right">24,8600</td><td align="right">24,8600</td><td class="numericspvar positive dropup" align="right">0,3200<i class="caret caret-small"></i></td>
			</tr><tr class="odd">
				<td align="left">18.01.2024</td><td align="left">REGS</td><td align="right">537</td><td align="right">177.389</td><td align="right">4.388.981,70</td><td align="right">24,7800</td><td align="right">24,6800</td><td align="right">24,8800</td><td align="right">24,7400</td><td align="right">24,7800</td><td class="numericspvar positive dropup" align="right">0,0800<i class="caret caret-small"></i></td>
			</tr><tr class="even">
				<td align="left">17.01.2024</td><td align="left">REGS</td><td align="right">610</td><td align="right">386.258</td><td align="right">9.608.842,90</td><td align="right">25,0000</td><td align="right">24,7600</td><td align="right">25,0000</td><td align="right">24,8800</td><td align="right">24,7600</td><td class="numericspvar negative" align="right">-0,6400<i class="caret caret-small"></i></td>
			</tr><tr class="odd">
				<td align="left">16.01.2024</td><td align="left">REGS</td><td align="right">723</td><td align="right">342.288</td><td align="right">8.518.881,52</td><td align="right">24,9000</td><td align="right">24,7000</td><td align="right">25,0400</td><td align="right">24,8800</td><td align="right">24,9200</td><td class="numericspvar positive dropup" align="right">0,1600<i class="caret caret-small"></i></td>
			</tr><tr class="even">
				<td align="left">15.01.2024</td><td align="left">REGS</td><td align="right">844</td><td align="right">666.430</td><td align="right">16.594.546,56</td><td align="right">24,9800</td><td align="right">24,8400</td><td align="right">25,0000</td><td align="right">24,9000</td><td align="right">24,8800</td><td class="numericspvar stable" align="right">0,0000<i class="fa fa-square fa-small"></i></td>
			</tr><tr class="odd">
				<td align="left">12.01.2024</td><td align="left">REGS</td><td align="right">677</td><td align="right">144.909</td><td align="right">3.613.271,58</td><td align="right">24,9000</td><td align="right">24,8200</td><td align="right">25,0000</td><td align="right">24,9400</td><td align="right">24,8800</td><td class="numericspvar positive dropup" align="right">0,3200<i class="caret caret-small"></i></td>
			</tr><tr class="even">
				<td align="left">11.01.2024</td><td align="left">REGS</td><td align="right">584</td><td align="right">142.193</td><td align="right">3.533.540,24</td><td align="right">24,8000</td><td align="right">24,7600</td><td align="right">24,9600</td><td align="right">24,8600</td><td align="right">24,8000</td><td class="numericspvar positive dropup" align="right">0,1600<i class="caret caret-small"></i></td>
			</tr></tbody>
	</table>
"""

# Parse the HTML content
soup = BeautifulSoup(html, 'html.parser')

# Find the table element
table = soup.find('table', {'id': 'gvSummar'})

# Extract column headers
headers = [th.text.strip() for th in table.find('thead').find_all('th')]

# Extract table rows
data = []
for row in table.find('tbody').find_all('tr'):
    row_data = [td.text.strip() for td in row.find_all('td')]
    data.append(row_data)

# Print column headers and data
print(headers)
for row in data:
    print(row)
