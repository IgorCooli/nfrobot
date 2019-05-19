import zeep
from zeep import Client
from zeep.wsse.signature import Signature

xml = """
        <GerarNfseEnvio xmlns="http://notacarioca.rio.gov.br/WSNacional/XSD/1/nfse_pcrj_v01.xsd">
            <Rps>
                <InfRps xmlns="http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd" Id="R1">
                <IdentificacaoRps>
                    <Numero>1</Numero>
                    <Serie>ABC</Serie>
                    <Tipo>1</Tipo>
                </IdentificacaoRps>
                <DataEmissao>2010-01-01T21:00:00</DataEmissao>
                <NaturezaOperacao>1</NaturezaOperacao>
                <OptanteSimplesNacional>2</OptanteSimplesNacional>
                <IncentivadorCultural>2</IncentivadorCultural>
                <Status>1</Status>
                <Servico>
                    <Valores>
                    <ValorServicos>1000.00</ValorServicos>
                    <ValorDeducoes>0</ValorDeducoes>
                    <ValorPis>10.00</ValorPis>
                    <ValorCofins>10.00</ValorCofins>
                    <ValorInss>10.00</ValorInss>
                    <ValorIr>10.00</ValorIr>
                    <ValorCsll>10.00</ValorCsll>
                    <IssRetido>2</IssRetido>
                    <ValorIss>10.00</ValorIss>
                    <OutrasRetencoes>10.00</OutrasRetencoes>
                    <Aliquota>0.05</Aliquota>
                    <DescontoIncondicionado>10.00</DescontoIncondicionado>
                    <DescontoCondicionado>10.00</DescontoCondicionado>
                    </Valores>
                    <ItemListaServico>0102</ItemListaServico>
                    <CodigoTributacaoMunicipio>010201</CodigoTributacaoMunicipio>
                    <Discriminacao>Teste</Discriminacao>
                    <CodigoMunicipio>3304557</CodigoMunicipio>
                </Servico>
                <Prestador>
                    <Cnpj>04642554000143</Cnpj>
                    <InscricaoMunicipal>2994275</InscricaoMunicipal>
                </Prestador>
                <Tomador>
                    <IdentificacaoTomador>
                    <CpfCnpj>
                        <Cnpj>99999999000191</Cnpj>
                    </CpfCnpj>
                    </IdentificacaoTomador>
                    <RazaoSocial>INSCRICAO DE TESTE</RazaoSocial>
                    <Endereco>
                    <Endereco>AV RIO BRANCO</Endereco>
                    <Numero>12345</Numero>
                    <Complemento>SALA 1001 1002</Complemento>
                    <Bairro>CENTRO</Bairro>
                    <CodigoMunicipio>3304557</CodigoMunicipio>
                    <Uf>RJ</Uf>
                    <Cep>20040001</Cep>
                    </Endereco>
                </Tomador>
                </InfRps>
                <Signature xmlns="http://www.w3.org/2000/09/xmldsig#">
                <SignedInfo>
                    <CanonicalizationMethod Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315" />
                    <SignatureMethod Algorithm="http://www.w3.org/2000/09/xmldsig#rsa-sha1" />
                    <Reference URI="#R1">
                    <Transforms>
                        <Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature" />
                        <Transform Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315" />
                    </Transforms>
                    <DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1" />
                    <DigestValue>pyuIXFAqQ0hwr+3cH2taKy0CGjk=</DigestValue>
                    </Reference>
                </SignedInfo>
                <SignatureValue>iHkS2259HxU7nFnJr1qnRA1YFuDPFH94k/TbqcXxOCISFL5vTeBY5AaV0fuUwY78/O1rczSv0pc+dNUTV2LexsSmplyyvlyDboXhPpR29Cvd2UWasAUAl4um1BLzKH322ustSNpKePbmhsMpkAIhZC3MVaCpUt4netvToveHrVA=</SignatureValue>
                <KeyInfo>
                    <X509Data>
                    <X509Certificate>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</X509Certificate>
                    </X509Data>
                </KeyInfo>
                </Signature>
            </Rps>
        </GerarNfseEnvio>
"""

client = Client('https://homologacao.notacarioca.rio.gov.br/WSNacional/nfse.asmx', wsse=Signature('cert.pem', 'key.pem'))

#print(client.service.nfdEntrada())
