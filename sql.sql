SELECT a.* ,

substr(obter_dados_pf_pj(null,cd_cnpj,'N'),1,254) DS_CLIENTE,

substr(obter_dados_com_cliente(nr_sequencia,'V'),1,2) IE_VINCULO,

substr(obter_dados_pf_pj(null, cd_cnpj, 'F'),1,254) NM_FANTASIA,

  substr(obter_dados_pf_pj(null,cd_cnpj,'N'),1,254) DS_EMPRESA,

  substr(obter_valor_dominio(1082,ie_natureza),1,254) DS_NATUREZA,

  substr(obter_valor_dominio(1314,ie_fase_venda),1,254) NM_FASE_VENDA,

  substr(obter_valor_dominio(1264,ie_status_neg),1,254) DS_STATUS,

  substr(obter_valor_dominio(1315,ie_classificacao),1,254) DS_CLASSIFICACAO,

  substr(obter_valor_dominio(1316,ie_tipo),1,254) DS_TIPO,

  substr(obter_descricao_padrao('COM_ATIVIDADE', 'DS_ATIVIDADE', nr_seq_ativ),1,255) DS_ATIVIDADE,

  to_date(substr(obter_dados_com_cliente(nr_sequencia,'UH'),1,19), 'dd/mm/yyyy hh24:mi:ss') DT_ULT_HISTORICO,

  substr(Com_obter_dados_lead(NR_SEQ_LEAD,'DFA'),1,255) DS_FORMA_AQUIS_LEAD,

  substr(obter_dados_pf_pj(null,CD_CNPJ,'DS_UF'),1,255) DS_ESTADO,

  substr(obter_dados_pf_pj(null,CD_CNPJ,'CI'),1,255) DS_CIDADE,

  substr(com_obter_canal_venda(nr_sequencia, 'D'), 1, 255) DS_CANAL,

  substr(obter_valor_dominio(2668, ie_produto),1,200) DS_PRODUTO,

  substr(obter_valor_dominio(5763,ie_migracao),1,254) DS_MIGRACAO,

  substr(obter_valor_dominio(8384,ie_segmentacao),1,254) DS_SEGMENTACAO,

  (SELECT substr(me.ds_equipamento,1,255) ds_equipamento

FROM man_equipamento me

WHERE me.ie_situacao = 'A'

and a.nr_seq_equip_audit = me.nr_sequencia) DS_EQUIP_AUDIT, substr(obter_valor_dominio(9080,IE_RECEBE_AUDITORIA),1,254) DS_RECEBE_AUDITORIA, substr(obter_dados_pf_pj(null,cd_cnpj,'N'),1,254) DS_RAZAO_SOCIAL_CLIENTE

FROM COM_CLIENTE a

WHERE 1 = 1 

 AND (dt_aprov_duplic is not null OR ie_etapa_duplic is null) 

 AND ie_situacao = 'A' 

 AND ie_classificacao = 'C' 

 AND cd_empresa = '1'

ORDER BY substr(obter_dados_pf_pj(null,cd_cnpj,'N'),1,254)