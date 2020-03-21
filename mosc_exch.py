stocks_by_groups= {'Золото/металлы':['POLY.ME','PLZL.ME','RUAL.ME','VSMO.ME','GMKN.ME','MAGN.ME','NLMK.ME','CHMF.ME','TRMK.ME'],
 'Алмазы':['ALRS.ME'],
 'Удобрения':['AKRN.ME','PHOR.ME'],
 'Авиаперевозки':['AFLT.ME'],
 'Нефть':['BANE.ME','BANEP.ME','LKOH.ME','ROSN.ME','SNGS.ME','SNGSP.ME','TATN.ME','TATNP.ME','TRNFP.ME'],
 'Банки':['VTBR.ME','CBOM.ME','SBER.ME','SBERP.ME'],
 'Энергия|Газ':['GAZP.ME','IRAO.ME','NVTK.ME','RSTI.ME','HYDR.ME','FEES.ME','UPRO.ME'],
 'Строительство|Девелопмент':['LSRG.ME','PIKK.ME'],
 'Ритейл':['LNTA.ME','MGNT.ME'],
 'Техника':['MVID.ME'],
 'Связь':['MTSS.ME','RTKMP.ME','RTKM.ME'],
 'Биржи':['MOEX.ME'],
 'Пластик':['NKNC.ME'],
 'Инвестиции':['AFKS.ME'],
 'Мясо':['GCHE.ME'],
 'ИТ':['YNDX.ME'],
}

def show_stocks():
    print()
    global stocks_by_groups
    for group in stocks_by_groups:
        print(group,' ',end='')
        print(" ".join(stocks_by_groups[group]))
    print()

show_stocks()
