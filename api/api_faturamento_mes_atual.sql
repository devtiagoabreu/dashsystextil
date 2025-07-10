/*
 * GET Url: http://promoda.systextil.com.br/apexbd/erp/systextil-intg-plm/api_faturamento_mes_atual
 * Credentials: OAuth 2
 * Grant Type: Client Credentials
 * Tag: faturamento
 */

 SELECT
   SUM(VALOR_SAIDA) AS VALOR_SAIDA,
   SUM(QTDE_SAIDA) AS QTDE_SAIDA
FROM 
  pmdvw_nfs
WHERE
  ENTRADA_SAIDA = 'Saida' and
  FATURAMENTO_SIM_NAO = 'Sim' and
  DATA_MOVTO BETWEEN TRUNC(SYSDATE, 'MM') AND LAST_DAY(SYSDATE)