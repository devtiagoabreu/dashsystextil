/*
 * GET Url: http://promoda.systextil.com.br/apexbd/erp/systextil-intg-plm/api_faturamento_mes_atual_por_dia
 * Credentials: OAuth 2
 * Grant Type: Client Credentials
 * Tag: faturamento
 */
SELECT
	 TO_CHAR(DATA_MOVTO, 'DD/MM/YYYY') AS DATA_MOVTO,
   SUM(VALOR_SAIDA) AS VALOR_SAIDA,
   SUM(QTDE_SAIDA) AS QTDE_SAIDA
FROM 
  pmdvw_nfs
WHERE
  ENTRADA_SAIDA = 'Saida' and
  FATURAMENTO_SIM_NAO = 'Sim' and
  DATA_MOVTO BETWEEN TRUNC(SYSDATE, 'MM') AND LAST_DAY(SYSDATE)
GROUP BY
	DATA_MOVTO
ORDER BY 
	DATA_MOVTO ASC