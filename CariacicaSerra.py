import zeep
from zeep import Client
from zeep.wsse.signature import Signature

xml = """
    
         <nfd><![CDATA[
					
			<tbnfd>
			<nfd>			
			<numeronfd>0</numeronfd>
			<codseriedocumento>8</codseriedocumento>
			<codnaturezaoperacao>511</codnaturezaoperacao>
			<codigocidade>3</codigocidade>
			<inscricaomunicipalemissor>113532</inscricaomunicipalemissor>
			<dataemissao>02/05/2019</dataemissao>
			<razaotomador>SMARapd ltda</razaotomador>
			<nomefantasiatomador> SMARapd </nomefantasiatomador>
			<enderecotomador>Rua Aurora</enderecotomador>
			<cidadetomador>Ribeirao Preto</cidadetomador>
			<estadotomador>SP</estadotomador>
			<paistomador>Brasil</paistomador>
			<fonetomador>21119898</fonetomador>
			<faxtomador/>
			<ceptomador>79010100</ceptomador>
			<bairrotomador>Centro</bairrotomador>
			<emailtomador>teste@smarapd.com.br</emailtomador>
			<cpfcnpjtomador>30669959085741</cpfcnpjtomador>
			<inscricaoestadualtomador/>
			<inscricaomunicipaltomador/>
			<tbfatura>
			<fatura>
			<numfatura>01</numfatura>
			<vencimentofatura>02/05/2019</vencimentofatura>
			<valorfatura>100</valorfatura>
			</fatura>
			<fatura>
			<numfatura>2</numfatura>
			<vencimentofatura>02/05/2019</vencimentofatura>
			<valorfatura>100</valorfatura>
			</fatura>
			<fatura>
			<numfatura>3</numfatura>
			<vencimentofatura>02/05/2019</vencimentofatura>
			<valorfatura>100</valorfatura>
			</fatura>
			</tbfatura>
			<tbservico>
			<servico>
			<quantidade>2</quantidade>
			<unidade>UN</unidade>
			<descricao>Servicos de Criacao de Logomarca</descricao>
			<codatividade>0702</codatividade>
			<valorunitario>150</valorunitario>
			<aliquota>2</aliquota>
			<impostoretido>False</impostoretido>
			</servico>
			<servico>
			<quantidade>1</quantidade>
			<unidade>UN</unidade>
			<descricao>Servicos de Criacao de Logomarca</descricao>
			<codatividade>0702</codatividade>
			<valorunitario>200</valorunitario>
			<aliquota>2</aliquota>
			<impostoretido>False</impostoretido>
			</servico>
			<servico>
			<quantidade>5</quantidade>
			<unidade>UN</unidade>
			<descricao>Servicos de Criacao de Logomarca</descricao>
			<codatividade>0702</codatividade>
			<valorunitario>150</valorunitario>
			<aliquota>2</aliquota>
			<impostoretido>False</impostoretido>
			</servico>
			</tbservico>
			<vlraproximposto>0</vlraproximposto>
			<aliquotaimpostoaprox>0</aliquotaimpostoaprox>
			<fonteimpostoaprox>IBPT</fonteimpostoaprox>
			<observacao>Pedido 3258943</observacao>
			<razaotransportadora/>
			<cpfcnpjtransportadora/>
			<enderecotransportadora/>
			<tipofrete>0</tipofrete>
			<quantidade>0</quantidade>
			<especie/>
			<pesoliquido>0</pesoliquido>
			<pesobruto>0</pesobruto>
			<pis/>
			<cofins/>
			<csll/>
			<irrf/>
			<inss/>
			<descdeducoesconstrucao/>
			<totaldeducoesconstrucao/>
			<tributadonomunicipio>true</tributadonomunicipio>
			<numerort/>
			<codigoseriert/>
			<dataemissaort/>
			</nfd>
			</tbnfd>			
         ]]></nfd>
"""

client = Client('http://servicos.cariacica.es.gov.br:8080/tbw/services/WSEntrada?wsdl', wsse=Signature('cert.pem', 'key.pem'))
#client = Client('http://servicos.cariacica.es.gov.br:8080/tbw/services/WSEntrada?wsdl')

print(client.service.nfdEntrada(cpfUsuario="55555555555", hashSenha="cRDtpNCeBiql5KOQsKVyrA0sAiA=", codigoMunicipio=3, nfd=xml))
