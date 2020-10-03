import csv

row_list = [["index", "name"],
            ["0", "半夏"],
            ["1", "柴胡"],
            ["2", "大黄"],
            ["3", "大枣"],
            ["4", "芍药"],
            ["5", "黄芩"],
            ["6", "生姜"],
            ["7", "枳实"],
            ["8", "人参"],
            ["9", "甘草"],
            ["10", "炙甘草"],
            ["11", "干姜"],
            ["12", "黄连"],
            ["13", "当归"],
            ["14", "茯苓"],
            ["15", "白芍"],
            ["16", "白术"],
            ["17", "陈皮"],
            ["18", "防风"],
            ["19", "槟榔"],
            ["20", "厚朴"],
            ["21", "草果仁"],
            ["22", "知母"],
            ["23", "青蒿脑"],
            ["24", "淡竹茹"],
            ["25", "仙半夏"],
            ["26", "赤茯苓"],
            ["27", "青子芩"],
            ["28", "生枳壳"],
            ["29", "陈广皮"],
            ["30", "碧玉散"],
            ["31", "滑石"],
            ["32", "青黛"],
            ["33", "款冬花"],
            ["34", "桑白皮"],
            ["35", "桔梗"],
            ["36", "五味子"],
            ["37", "阿胶"],
            ["38", "乌梅"],
            ["39", "贝母"],
            ["40", "罂粟壳"],
            ["41", "肉豆蔻"],
            ["42", "补骨脂"],
            ["43", "吴茱萸"],
            ["44", "红枣"],
            ["45", "黄芪"],
            ["46", "麻黄根"],
            ["47", "牡蛎米"],
            ["48", "小麦"],
            ["49", "生黄芪"],
            ["50", "龙骨"],
            ["51", "牡蛎"],
            ["52", "山茱萸"],
            ["53", "生白芍"],
            ["54", "海螵蛸"],
            ["55", "茜草"],
            ["56", "棕边炭"],
            ["57", "五倍子"],
            ["58", "龟板"],
            ["59", "黄柏"],
            ["60", "椿树根皮"],
            ["61", "香附"],
            ["62", "山药"],
            ["63", "芡实"],
            ["64", "车前子"],
            ["65", "白果"],
            ["66", "沙苑蒺藜"],
            ["67", "莲须"],
            ["68", "桑螵蛸"],
            ["69", "远志"],
            ["70", "菖蒲"],
            ["71", "茯神"],
            ["72", "龟甲"],
            ["73", "肉桂"],
            ["74", "木香"],
            ["75", "诃子"],
            ["76", "玄参"],
            ["77", "丹参"],
            ["78", "麦门冬"],
            ["79", "天门冬"],
            ["80", "柏子仁"],
            ["81", "酸枣仁"],
            ["82", "生地黄"],
            ["83", "朱砂"],
            ["84", "川芎"],
            ["85", "牛黄"],
            ["86", "郁金"],
            ["87", "山栀"],
            ["88", "雄黄"],
            ["89", "犀角"],
            ["90", "冰片"],
            ["91", "麝香"],
            ["92", "珍珠"],
            ["93", "生玳瑁"],
            ["94", "琥珀"],
            ["95", "安息香"],
            ["96", "石膏"],
            ["97", "寒水石"],
            ["98", "磁石"],
            ["99", "羚羊角"],
            ["100", "沉香"],
            ["101", "升麻"],
            ["102", "丁香"],
            ["103", "苏合香"],
            ["104", "乳香"],
            ["105", "白檀香"],
            ["106", "荜茇"],
            ["107", "诃子皮"],
            ["108", "龟版胶"],
            ["109", "生地"],
            ["110", "麦冬"],
            ["111", "百合"],
            ["112", "苏叶"],
            ["113", "前胡"],
            ["114", "苦桔梗"],
            ["115", "枳壳"],
            ["116", "杏仁"],
            ["117", "橘皮"],
            ["118", "桑叶"],
            ["119", "沙参"],
            ["120", "象贝"],
            ["121", "香豉"],
            ["122", "栀皮"],
            ["123", "梨皮"],
            ["124", "冰糖"],
            ["125", "细生地"],
            ["126", "玉竹"],
            ["127", "胡麻仁"],
            ["129", "真阿胶"],
            ["130", "枇杷叶"],
            ["131", "粳米"],
            ["132", "大生地"],
            ["133", "白芥子"],
            ["134", "丹皮"],
            ["135", "薄荷"],
            ["136", "白芍炒"],
            ["137", "生龟板"],
            ["138", "干地黄"],
            ["139", "麻仁"],
            ["140", "生牡蛎"],
            ["141", "鸡子黄"],
            ["142", "鳖甲"],
            ["143", "秦艽"],
            ["144", "细辛"],
            ["145", "川羌活"],
            ["146", "白芷"],
            ["147", "熟地黄"],
            ["148", "白茯苓"],
            ["149", "川独活"],
            ["150", "炮川乌"],
            ["151", "炮草乌"],
            ["152", "地龙"],
            ["153", "炮天南星"],
            ["154", "没药"],
            ["155", "荆芥"],
            ["156", "羌活"],
            ["157", "薄荷叶"],
            ["158", "天麻"],
            ["159", "钩藤"],
            ["160", "生决明"],
            ["161", "川牛膝"],
            ["162", "杜仲"],
            ["163", "益母草"],
            ["164", "桑寄生"],
            ["165", "夜交藤"],
            ["166", "朱茯神"],
            ["167", "南星"],
            ["168", "白附子"],
            ["169", "蝉蜕"],
            ["170", "苦参"],
            ["171", "胡麻"],
            ["172", "苍术"],
            ["173", "牛蒡子"],
            ["174", "木通"],
            ["175", "白僵蚕"],
            ["176", "全蝎"],
            ["177", "羚角片"],
            ["178", "霜桑叶"],
            ["179", "京贝母"],
            ["180", "鲜生地"],
            ["181", "双钩藤"],
            ["182", "滁菊花"],
            ["183", "茯神木"],
            ["184", "怀牛膝"],
            ["185", "生赭石"],
            ["186", "生龙骨"],
            ["187", "生杭芍"],
            ["188", "天冬"],
            ["189", "川楝子"],
            ["190", "生麦芽"],
            ["191", "茵陈"],
            ["192", "芫花"],
            ["193", "甘遂"],
            ["194", "大戟"],
            ["195", "芒硝"],
            ["196", "牡丹"],
            ["197", "桃仁"],
            ["198", "冬瓜仁"],
            ["199", "炮附子"],
            ["200", "麻子仁"],
            ["201", "附子"],
            ["202", "牛膝"],
            ["203", "肉苁蓉"],
            ["204", "泽泻"],
            ["205", "山楂"],
            ["206", "神曲"],
            ["207", "连翘"],
            ["208", "莱菔子"],
            ["209", "砂仁"],
            ["210", "麦芽"],
            ["211", "猪苓"],
            ["212", "青皮"],
            ["213", "缩砂仁"],
            ["214", "白豆蔻仁"],
            ["215", "葛花"],
            ["216", "炙厚朴"],
            ["217", "瓜蒂"],
            ["218", "赤小豆"],
            ["219", "穿山甲"],
            ["220", "赤芍药"],
            ["221", "当归梢"],
            ["222", "天花粉"],
            ["223", "皂角刺"],
            ["224", "金银花"],
            ["225", "白头翁"],
            ["226", "秦皮"],
            ["227", "竹叶"],
            ["228", "官桂"],
            ["229", "青蒿"],
            ["230", "朴硝"],
            ["231", "栀子"],
            ["232", "当归身"],
            ["233", "牡丹皮"],
            ["234", "银柴胡"],
            ["235", "胡黄连"],
            ["236", "鳖甲"],
            ["237", "地骨皮"],
            ["238", "元参"],
            ["239", "竹叶心"],
            ["240", "板蓝根"],
            ["241", "马勃"],
            ["242", "僵蚕"],
            ["243", "苇茎"],
            ["244", "薏苡仁"],
            ["245", "瓜瓣"],
            ["246", "葛根"],
            ["247", "甘草梢"],
            ["248", "龙胆草"],
            ["249", "桂枝"],
            ["250", "胶饴"],
            ["251", "熟附子"],
            ["252", "白术炒"],
            ["253", "半夏制"],
            ["254", "麻黄"],
            ["255", "鹿角胶"],
            ["256", "白芥子"],
            ["257", "炮姜炭"],
            ["258", "通草"],
            ["259", "乌药"],
            ["260", "小茴香"],
            ["261", "高良姜"],
            ["262", "巴豆"],
            ["263", "苏子"],
            ["264", "法制半夏"],
            ["265", "金铃子"],
            ["266", "玄胡"],
            ["267", "草豆蔻"],
            ["268", "旋覆花"],
            ["269", "代赭石"],
            ["270", "枸杞子"],
            ["271", "竹茹"],
            ["272", "紫苏子"],
            ["273", "川当归"],
            ["274", "甘草爁"],
            ["275", "姜汁"],
            ["276", "薤白"],
            ["277", "瓜蒌实"],
            ["278", "大蓟"],
            ["279", "小蓟"],
            ["280", "荷叶"],
            ["281", "侧柏叶"],
            ["282", "茅根"],
            ["283", "茜根"],
            ["284", "棕榈皮"],
            ["285", "蒲黄"],
            ["286", "藕节"],
            ["287", "淡竹叶"],
            ["288", "山栀子"],
            ["289", "五灵脂"],
            ["290", "干姜炮"],
            ["291", "红花"],
            ["292", "瓜蒌仁"],
            ["293", "海粉"],
            ["294", "瓜蒌根"],
            ["295", "灶心黄土"],
            ["296", "槐花"],
            ["297", "柏叶"],
            ["298", "荆芥穗"],
            ["299", "乌扇"],
            ["300", "鼠妇"],
            ["301", "石韦"],
            ["302", "紫葳"],
            ["303", "蜣螂"],
            ["304", "䗪虫"],
            ["305", "蜂窠"],
            ["306", "赤硝"],
            ["307", "瞿麦"],
            ["308", "葶苈"],
            ["309", "香薷"],
            ["310", "白扁豆"],
            ["311", "西洋参"],
            ["312", "石斛"],
            ["313", "荷梗"],
            ["314", "西瓜翠衣"],
            ["315", "鲜荷叶边"],
            ["316", "鲜银花"],
            ["317", "丝瓜皮"],
            ["318", "鲜扁豆花"],
            ["319", "鲜竹叶心"],
            ["320", "萹蓄"],
            ["321", "山栀子仁"],
            ["322", "飞滑石"],
            ["323", "白通草"],
            ["324", "白蔻仁"],
            ["325", "生薏苡仁"],
            ["326", "生姜皮"],
            ["327", "陈橘皮"],
            ["328", "大腹皮"],
            ["329", "茯苓皮"],
            ["330", "淡黄芩"],
            ["331", "绵茵陈"],
            ["332", "石菖蒲"],
            ["333", "川贝母"],
            ["334", "藿香"],
            ["335", "射干"],
            ["335", "防已"],
            ["336", "独活"],
            ["337", "槁本"],
            ["338", "蔓荆子"],
            ["339", "制厚朴"],
            ["340", "川连"],
            ["341", "焦栀"],
            ["342", "芦根"],
            ["343", "木瓜"],
            ["344", "大腹子"],
            ["345", "肉桂心"],
            ["346", "益智"],
            ["347", "川萆薢"],
            ["348", "紫苏"],
            ["349", "橘红"],
            ["350", "生甘草"],
            ["351", "瓜蒌"],
            ["352", "花粉"],
            ["353", "明天麻"],
            ["354", "胆南星"],
            ["355", "辰砂"],
            ["356", "礞石"],
            ["357", "风化朴硝"],
            ["358", "北沙参"],
            ["359", "白芍药"],
            ["360", "龟版"],
            ["361", "山萸肉"],
            ["362", "干山药"],
            ["363", "山药炒"],
            ["364", "菟丝子"],
            ["365", "制附子"],
            ["366", "巴戟天"],
            ["367", "黑芥穗"],
            ["368", "莲子肉"],
            ["369", "鹿角"],
            ["370", "香白芷"],
            ["371", "紫菀"],
            ["372", "百部"],
            ["373", "白前"],
            ["374", "葱白"],
            ["375", "东白薇"],
            ["376", "淡豆豉"],
            ["377", "苏薄荷"],
            ["378", "香附子"],
            ["379", "紫苏叶"],
            ["380", "干葛"],
            ["381", "蜀椒"],
            ["1000","未知药"]]

with open('IndexName.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(row_list)
