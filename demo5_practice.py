#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import re

content = requests.get('https://book.douban.com/latest?icn=index-latestbook-all').text
print(content)
# 下面的content来源自print（content）
content = '''
            <li>
                <a class="cover" href="https://book.douban.com/subject/27611824/"><img src="https://img3.doubanio.com/view/subject/m/public/s29707420.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/27611824/">如父如子</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar45"></span> 
                        <span class="font-small  color-lightgray">
                                8.9
                        </span>
                    </p>
                    <p class="color-gray">
                        [日] 是枝裕和 / [日] 佐野晶 / 湖南文艺出版社 / 2018-4
                    </p>
                    <p class="detail">
                        日本电影大师是枝裕和真情流露之作，第66届戛纳电影节评审团奖同名小说，贯通千千万万家庭的亲子温情物语。        
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/27201424/"><img src="https://img3.doubanio.com/view/subject/m/public/s29719811.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/27201424/">无人幸免</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar45"></span> 
                        <span class="font-small  color-lightgray">
                                8.5
                        </span>
                    </p>
                    <p class="color-gray">
                        [加] 奥马尔·阿卡德 / 未读·北京联合出版公司 / 2018-3
                    </p>
                    <p class="detail">
                        2017年美国现象级小说，大胆虚构了发生在2074年的美国的第二次南北战争，一部将战争报道和反乌托邦题材巧妙结合的佳作，《纽约时报》年度瞩目好书。       
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/27620790/"><img src="https://img3.doubanio.com/view/subject/m/public/s29708821.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/27620790/">青梅竹马</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar40"></span> 
                        <span class="font-small  color-lightgray">
                                7.5
                        </span>
                    </p>
                    <p class="color-gray">
                        [日] 樋口一叶 / 百花洲文艺出版社 / 2018-3
                    </p>
                    <p class="detail">
                        本书精选了日本明治时期女作家樋口一叶的十篇短篇小说，是初恋文学的传世经典著作，人气作者小岩井倾情翻译。        
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/30128189/"><img src="https://img1.doubanio.com/view/subject/m/public/s29742739.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/30128189/">红发女人</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar40"></span> 
                        <span class="font-small  color-lightgray">
                                7.8
                        </span>
                    </p>
                    <p class="color-gray">
                        [土耳其] 奥尔罕·帕慕克 / 世纪文景 | 上海人民出版社 / 2018-4
                    </p>
                    <p class="detail">
                        诺贝尔文学奖得主奥尔罕·帕慕克首次尝试“写一部更短的小说”，向着记忆的幽暗深处一路挖掘的心灵之旅，获2017年意大利兰佩杜萨国际文学奖。       
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/27666853/"><img src="https://img3.doubanio.com/view/subject/m/public/s29682061.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/27666853/">梦的花嫁</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar45"></span> 
                        <span class="font-small  color-lightgray">
                                8.7
                        </span>
                    </p>
                    <p class="color-gray">
                        [日] 岩井俊二 / 南海出版公司 / 2018-3
                    </p>
                    <p class="detail">
                        日本著名导演岩井俊二推出的全新长篇小说，一场闪婚带来的种种迷局，书写世间的爱与希望，改编电影入选日本年度十大电影。        
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/27605425/"><img src="https://img3.doubanio.com/view/subject/m/public/s29669644.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/27605425/">吉姆</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar45"></span> 
                        <span class="font-small  color-lightgray">
                                8.9
                        </span>
                    </p>
                    <p class="color-gray">
                        [英] 鲁德亚德·吉卜林 / 浙江文艺出版社 / 2018-3
                    </p>
                    <p class="detail">
                        英国首位诺贝尔文学奖得主吉卜林代表作，一个孤儿与一位喇嘛寻找箭河的冒险之旅，入选世界百大经典英文小说。        
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/27622647/"><img src="https://img1.doubanio.com/view/subject/m/public/s29702987.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/27622647/">法国往事6：应许之地</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar45"></span> 
                        <span class="font-small  color-lightgray">
                                9.3
                        </span>
                    </p>
                    <p class="color-gray">
                        [法] 法比安·努瑞 文 / 西尔万·瓦雷 图 / 后浪丨四川人民出版社 / 2018-4
                    </p>
                    <p class="detail">
                        《法国往事》六部曲传记体史诗大结局，新旧人物纷纷登场、谢幕，“乱世枭雄”约瑟夫·乔诺维奇传奇人生的最终乐章，折射一个时代的风云变幻。
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/30183433/"><img src="https://img3.doubanio.com/view/subject/m/public/s29728432.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/30183433/">公鸡王子</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar50"></span> 
                        <span class="font-small  color-lightgray">
                                9.8
                        </span>
                    </p>
                    <p class="color-gray">
                        双翅目 / 东方出版社 / 2018-4
                    </p>
                    <p class="detail">
                        “豆瓣阅读征文大赛”科幻组首奖得主双翅目首部中短篇科幻集，以东方哲学反思机器人三定律，用冷峻笔调速写技术寓言。       
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/27600499/"><img src="https://img3.doubanio.com/view/subject/m/public/s29731181.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/27600499/">乡下的葬礼</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar00"></span> 
                        <span class="font-small  color-lightgray">
                                评价人数不足
                        </span>
                    </p>
                    <p class="color-gray">
                        [爱尔兰] 约翰·麦加恩/著 / [爱尔兰] 科尔姆·托宾/编 / 人民文学出版社 / 2018-3
                    </p>
                    <p class="detail">
                        有“爱尔兰的契诃夫”之称的已故小说家约翰·麦加恩的短篇小说集，由当代著名爱尔兰作家科尔姆·托宾选编，详细介绍了约翰·麦加恩的短篇小说创作及其风格。
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/27109098/"><img src="https://img1.doubanio.com/view/subject/m/public/s29707057.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/27109098/">系统的笤帚</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar00"></span> 
                        <span class="font-small  color-lightgray">
                                
                        </span>
                    </p>
                    <p class="color-gray">
                        [美] 大卫·福斯特·华莱士 / 北京时代华文书局 / 2018-5-1
                    </p>
                    <p class="detail">
                        美国天才作家大卫·福斯特·华莱士25岁时创作的处女作，用极端理性的语言描绘复杂的现代社会和畸形的人性感情，影响美国的12部经典文学作品之一。        
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/30167202/"><img src="https://img3.doubanio.com/view/subject/m/public/s29728486.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/30167202/">山本</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar40"></span> 
                        <span class="font-small  color-lightgray">
                                8.4
                        </span>
                    </p>
                    <p class="color-gray">
                        贾平凹 / 人民文学出版社 / 2018-4
                    </p>
                    <p class="detail">
                        著名作家贾平凹的第16部长篇小说，是他酝酿多年立意为秦岭做传、为近代中国勾勒记忆的史诗巨著，一部震撼人心的民间秘史。       
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/28171580/"><img src="https://img3.doubanio.com/view/subject/m/public/s29725172.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/28171580/">人间便利店</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar40"></span> 
                        <span class="font-small  color-lightgray">
                                8.2
                        </span>
                    </p>
                    <p class="color-gray">
                        [日] 村田沙耶香 / 湖南文艺出版社·向上文学品牌 / 2018-4
                    </p>
                    <p class="detail">
                        持续了18年便利店人生的古仓惠子，平淡的生活在某天终被打破。日本第155届芥川奖获奖作品，引起日本社会集体沉思的现实主义话题之作。       
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/27611177/"><img src="https://img3.doubanio.com/view/subject/m/public/s29708651.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/27611177/">隔壁的女人</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar40"></span> 
                        <span class="font-small  color-lightgray">
                                7.9
                        </span>
                    </p>
                    <p class="color-gray">
                        [日] 向田邦子 / 文治图书·中国友谊出版公司 / 2018-3
                    </p>
                    <p class="detail">
                        日本国民偶像、编剧女王向田邦子短篇杰作精选，以敏锐细腻、坚韧优雅的女性力量，写尽了日常细节下的人性根底。        
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/27602493/"><img src="https://img3.doubanio.com/view/subject/m/public/s29685643.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/27602493/">不存在的情人</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar45"></span> 
                        <span class="font-small  color-lightgray">
                                9.1
                        </span>
                    </p>
                    <p class="color-gray">
                        [英] 海伦·奥耶耶美 / 中信出版集团 / 2018-3-1
                    </p>
                    <p class="detail">
                        《格兰塔》英国重量级青年小说家海伦·奥耶耶美突破之作，一场瑰丽诡谲的爱情冒险，《纽约时报》2011年度重点关注图书。        
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/27621482/"><img src="https://img3.doubanio.com/view/subject/m/public/s29721032.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/27621482/">折断的龙骨</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar45"></span> 
                        <span class="font-small  color-lightgray">
                                8.6
                        </span>
                    </p>
                    <p class="color-gray">
                        [日] 米泽穗信 / 现代出版社 / 2018-3-1
                    </p>
                    <p class="detail">
                        不按常理出牌的推理小说家米泽穗信经典作品，一个信仰的动摇  一个时代的阴影，第六十四届日本推理作家协会奖作品。        
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/30183465/"><img src="https://img3.doubanio.com/view/subject/m/public/s29728465.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/30183465/">追逐太阳的男人</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar45"></span> 
                        <span class="font-small  color-lightgray">
                                9.1
                        </span>
                    </p>
                    <p class="color-gray">
                        翼走 / 东方出版社 / 2018-4
                    </p>
                    <p class="detail">
                        豆瓣阅读征文大赛科幻组首奖得主翼走的首部中短篇科幻集，五个风格各异的故事，展示科幻的浪漫、优美和理想主义。        
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/30169891/"><img src="https://img3.doubanio.com/view/subject/m/public/s29714363.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/30169891/">追踪师</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar45"></span> 
                        <span class="font-small  color-lightgray">
                                8.5
                        </span>
                    </p>
                    <p class="color-gray">
                        紫金陈 / 中国友谊出版公司 / 2018-4-1
                    </p>
                    <p class="detail">
                        华语推理大神紫金陈重磅新作，一个精心设计的完美犯罪故事，国内首部以电子刑侦为主题的推理小说。      
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/30142261/"><img src="https://img3.doubanio.com/view/subject/m/public/s29738720.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/30142261/">长日将尽</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar00"></span> 
                        <span class="font-small  color-lightgray">
                                评价人数不足
                        </span>
                    </p>
                    <p class="color-gray">
                        [英] 石黑一雄 / 上海译文出版社 / 2018-5-1
                    </p>
                    <p class="detail">
                        2017诺贝尔文学奖得主石黑一雄代表作，布克奖获奖小说，以管家史蒂文斯的回忆展开，唱响一曲帝国衰落的挽歌，追述一场擦肩而过的爱情。
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/29965101/"><img src="https://img3.doubanio.com/view/subject/m/public/s29672352.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/29965101/">五个街角</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar00"></span> 
                        <span class="font-small  color-lightgray">
                                评价人数不足
                        </span>
                    </p>
                    <p class="color-gray">
                        [秘鲁] 马里奥·巴尔加斯·略萨 / 人民文学出版社 / 2018-4
                    </p>
                    <p class="detail">
                        诺贝尔文学奖得主马里奥·巴尔加斯·略萨最新长篇小说，一则爆炸性八卦引发的政商暗战，多重立体地呈现了令人瞠目结舌、大开眼界的当代都市众生相。        
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/27600483/"><img src="https://img3.doubanio.com/view/subject/m/public/s29724680.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/27600483/">小小陌生人</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar00"></span> 
                        <span class="font-small  color-lightgray">
                                评价人数不足
                        </span>
                    </p>
                    <p class="color-gray">
                        [英] 萨拉·沃特斯 / 上海人民出版社 / 2018-4
                    </p>
                    <p class="detail">
                        《指匠》作者萨拉·沃特斯暗黑哥特风小说，描绘上流阶层荣耀不再的英国战后社会，入围“布克奖”决选名单，《纽约时报》年度畅销书。        
                    </p>
                </div>
            </li>
    </ul>
    </div>

            

    <div class="aside">
    <h2 class="pl20">非虚构类  · · · · · · </h2>
    <ul class="cover-col-4 pl20 clearfix">
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/30177380/"><img src="https://img3.doubanio.com/view/subject/m/public/s29721851.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/30177380/">特工训练手册</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar40"></span> 
                        <span class="font-small color-lightgray">
                                8.0
                        </span>
                    </p>
                    <p class="color-gray">
                        [美] 克林特·埃默森 / 后浪丨民主与建设出版社 / 2018-4
                    </p>
                    <p>
                        前海豹突击队精英队员为你带来的紧要关头应急攻略，86招逃生秘籍，350幅精彩插图，帮助你建立危机意识，军事求生爱好者的福利。        
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/27622170/"><img src="https://img3.doubanio.com/view/subject/m/public/s29690393.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/27622170/">纽约：一座超级城市是如何运转的</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar45"></span> 
                        <span class="font-small color-lightgray">
                                8.8
                        </span>
                    </p>
                    <p class="color-gray">
                        [美] 凯特·阿歇尔 / 南海出版公司 / 2018-4
                    </p>
                    <p>
                        纽约的每一天都是现代文明的奇迹，这座城市的运转就像一个巨型魔术。一本解读繁华都市运转奥秘的百科全书，探索现代都市背后的奥秘。        
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/30134794/"><img src="https://img3.doubanio.com/view/subject/m/public/s29681403.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/30134794/">天才假象</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar45"></span> 
                        <span class="font-small color-lightgray">
                                9.3
                        </span>
                    </p>
                    <p class="color-gray">
                        [英] 马修·萨伊德 / 后浪丨江西人民出版社 / 2018-3
                    </p>
                    <p>
                        知名媒体人马修·萨伊德将体育训练思维引入成功心理研究，通过自身经验和旁征博引，将各个领域内的天才神话一一击破，证明长期刻意练习对成功的作用。       
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/30170099/"><img src="https://img1.doubanio.com/view/subject/m/public/s29721129.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/30170099/">如何看懂艺术</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar50"></span> 
                        <span class="font-small color-lightgray">
                                9.7
                        </span>
                    </p>
                    <p class="color-gray">
                        翁昕 / 未读·艺术家·北京联合出版公司 / 2018-4
                    </p>
                    <p>
                        艺术经纪人翁昕趣讲艺术的第一辑，零门槛的趣味艺术观赏指南，带领读者“亲临”艺术现场，生动讲述艺术品诞生的时代背景与创作故事。        
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/27667777/"><img src="https://img3.doubanio.com/view/subject/m/public/s29717573.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/27667777/">广州贸易</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar00"></span> 
                        <span class="font-small color-lightgray">
                                目前无人评价
                        </span>
                    </p>
                    <p class="color-gray">
                        [美] 范岱克 / 社会科学文献出版社 / 2018-4
                    </p>
                    <p>
                        一部了解清代对外贸易的经典著作，作者范岱克利用极为丰富的多语种资料，重建了广州贸易在18~19世纪上半叶的日常运作，是广州海外贸易体制研究的重要突破。       
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/27598734/"><img src="https://img3.doubanio.com/view/subject/m/public/s29713702.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/27598734/">审问欧洲</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar50"></span> 
                        <span class="font-small color-lightgray">
                                9.8
                        </span>
                    </p>
                    <p class="color-gray">
                        [美] 伊斯特万·迪克 / 中信出版集团 / 2018-3-1
                    </p>
                    <p>
                        战争摧毁了人性，还是人性引燃了战争？历史学家伊斯特万·迪克探究了第二次世界大战时期的合作、抵抗与报复，理清战时和战后的种种道德因果。        
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/30155966/"><img src="https://img1.doubanio.com/view/subject/m/public/s29703019.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/30155966/">翻译研究</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar45"></span> 
                        <span class="font-small color-lightgray">
                                9.1
                        </span>
                    </p>
                    <p class="color-gray">
                        思果 / 理想国 | 广西师范大学出版社 / 2018-3
                    </p>
                    <p>
                        著名散文家、翻译家思果的经验之谈，享誉港台四十余年，列举大量实例专治劣译和欧化中文，余光中先生专文推荐，一部译者的“自诊书”。        
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/30151815/"><img src="https://img3.doubanio.com/view/subject/m/public/s29744502.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/30151815/">月亮的另一面</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar00"></span> 
                        <span class="font-small color-lightgray">
                                评价人数不足
                        </span>
                    </p>
                    <p class="color-gray">
                        [法] 克洛德·列维-斯特劳斯 / 中国人民大学出版社 / 2018-3-15
                    </p>
                    <p>
                        收录了著名人类学家克洛德·列维-斯特劳斯于1979年至2001年发表的关于日本的人类学、神话学研究的演讲稿及文章，揭示月亮另一面的日本其文化独特的一面。        
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/27040920/"><img src="https://img3.doubanio.com/view/subject/m/public/s29705003.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/27040920/">地下巴黎</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar40"></span> 
                        <span class="font-small color-lightgray">
                                7.6
                        </span>
                    </p>
                    <p class="color-gray">
                        [法] 洛朗·多伊奇 / 上海译文出版社 / 2018-3
                    </p>
                    <p>
                        21个地铁站，21个世纪，冷知识、小八卦，一本别开生面的巴黎旅游手册，地道巴黎人作者洛朗·多伊奇带你玩出不一样的巴黎。        
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/30162141/"><img src="https://img3.doubanio.com/view/subject/m/public/s29708145.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/30162141/">日常天才</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar00"></span> 
                        <span class="font-small color-lightgray">
                                评价人数不足
                        </span>
                    </p>
                    <p class="color-gray">
                        [美] 盖瑞·阿兰·法恩 / 译林出版社 / 2018-3
                    </p>
                    <p>
                        为何非主流的艺术家往往受到更多关注？本书的研究对象正是位于艺术界边缘的非主流艺术类型，是对这个网络及其如何赋予艺术品价值的卓越洞见。         
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/30164685/"><img src="https://img1.doubanio.com/view/subject/m/public/s29710387.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/30164685/">网：阿加西自传</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar45"></span> 
                        <span class="font-small color-lightgray">
                                9.4
                        </span>
                    </p>
                    <p class="color-gray">
                        [美] 安德烈·阿加西 / 上海文化出版社 / 2018-4
                    </p>
                    <p>
                        网球历史上个性最复杂、经历最传奇的球星阿加西动人心魄的成长故事，被《时代周刊》誉为“史上最佳传记作品之一”。        
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/30157369/"><img src="https://img3.doubanio.com/view/subject/m/public/s29704940.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/30157369/">潘金莲的饺子</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar40"></span> 
                        <span class="font-small color-lightgray">
                                7.8
                        </span>
                    </p>
                    <p class="color-gray">
                        李舒 著 / 戴敦邦 绘 / 中信出版集团/楚尘文化 / 2018-3-31
                    </p>
                    <p>
                        《山河小岁月》《民国太太的厨房》作者李舒全新力作，以前所未有的方式写尽《金瓶梅》中的吃与“痴” ，重现小说成书时代晚明的真实生活景象。       
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/27122365/"><img src="https://img3.doubanio.com/view/subject/m/public/s29731620.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/27122365/">秦淮之夜</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar45"></span> 
                        <span class="font-small color-lightgray">
                                9.2
                        </span>
                    </p>
                    <p class="color-gray">
                        [日] 谷崎润一郎 / 浙江文艺出版社 / 2018-3
                    </p>
                    <p>
                        收录日本唯美派文学大师谷崎润一郎于1918、1926年两次游历中国后，写作的游记、日记、散文等作品，在山水衣食中细品“中国趣味” 。        
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/27036902/"><img src="https://img3.doubanio.com/view/subject/m/public/s29668983.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/27036902/">染匠之手</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar00"></span> 
                        <span class="font-small color-lightgray">
                                评价人数不足
                        </span>
                    </p>
                    <p class="color-gray">
                        [英] W·H·奥登 / 上海译文出版社 / 2018-3
                    </p>
                    <p>
                        收录一代文学巨匠W.H.奥登精彩纷呈的散文作品，是奥登这部文学批评代表作的首部完整中译本，二十世纪欧美文学批评领域的不朽巨著。        
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/27602487/"><img src="https://img3.doubanio.com/view/subject/m/public/s29673785.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/27602487/">中国思想史</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar00"></span> 
                        <span class="font-small color-lightgray">
                                评价人数不足
                        </span>
                    </p>
                    <p class="color-gray">
                        [法] 程艾蓝 / 河南大学出版社 / 2018-3
                    </p>
                    <p>
                        法国知名学者程艾兰的中国思想史著作，曾获1998年西方汉学最高奖儒莲奖，从中、西方双重视角审视中国思想，梳理了从商朝到五四运动间中国思想的演变。        
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/30136980/"><img src="https://img1.doubanio.com/view/subject/m/public/s29686339.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/30136980/">银盐时代</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar50"></span> 
                        <span class="font-small color-lightgray">
                                9.7
                        </span>
                    </p>
                    <p class="color-gray">
                        [美] 约翰·洛恩加德 / 后浪丨湖南美术出版社 / 2018-3
                    </p>
                    <p>
                        美国著名摄影师约翰· 洛恩加德用镜头关注半个世纪以来众多享有盛名的摄影师，从经典作品的银盐底片窥见大师们的创作过程。 
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/30164677/"><img src="https://img1.doubanio.com/view/subject/m/public/s29710377.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/30164677/">我们为什么会生病</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar00"></span> 
                        <span class="font-small color-lightgray">
                                评价人数不足
                        </span>
                    </p>
                    <p class="color-gray">
                        [美] 伦道夫·M·尼斯 / [美] 乔治·C·威廉斯 / 湖南科学技术出版社 / 2018-3
                    </p>
                    <p>
                        本书作者以演化的视野系统地观察医学领域，从演化的视角审视人体、疾病、衰老等健康议题，为思考疾病问题提供了全新的观念。       
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/27591360/"><img src="https://img3.doubanio.com/view/subject/m/public/s29712876.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/27591360/">诚品时光</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar45"></span> 
                        <span class="font-small color-lightgray">
                                8.6
                        </span>
                    </p>
                    <p class="color-gray">
                        林静宜 / 中信出版集团·见识城邦 / 2018-3
                    </p>
                    <p>
                        本书作者林静宜亲访创始人吴清友及核心团队，完整记录了台湾诚品书店从创办至今28年的风雨历程，倾情书写诚品经营始终不变的人文关怀。         
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/27189923/"><img src="https://img3.doubanio.com/view/subject/m/public/s29704085.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/27189923/">奇迹之书</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar45"></span> 
                        <span class="font-small color-lightgray">
                                9.0
                        </span>
                    </p>
                    <p class="color-gray">
                        [美] 杰夫·范德米尔 / [美] 杰里米·泽尔弗斯 / 新星出版社 / 2018-3
                    </p>
                    <p>
                        一本图文并茂的幻想文学创作指南，资深出版人、星云奖桂冠作家杰夫·范德米尔写作课程完全呈现，披露乔治·R.R.马丁、尼尔·盖曼十余位著名作家创作心得。     
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/27661659/"><img src="https://img3.doubanio.com/view/subject/m/public/s29742753.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/27661659/">纸上寻仙记</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar40"></span> 
                        <span class="font-small color-lightgray">
                                8.1
                        </span>
                    </p>
                    <p class="color-gray">
                        锦翼 / 上海文艺出版社 / 2018-4
                    </p>
                    <p>
                        作者锦翼从各类中国传统笔记体小说汲取灵感和素材，经过大量考据，以吃喝、拉撒、穿戴、出行的四个角度来讨论人、鬼、仙、妖的各类民间八卦。
        
                    </p>
                </div>
            </li>
     </ul>
'''
# 正则表达式的书写
pattern = re.compile('<li>.*?cover.*?href="(.*?)".*?detail-frame.*?<a.*?(.*?)</a>.*?color-lightgray">(.*?)</span>.*?color-gray">(.*?)</p>.*?</li>', re.S)
results = re.findall(pattern, content)
print(results)
for result in results:
    url, name, ranting, info = result
    print(url.strip(), name.strip(), ranting.strip(), info.strip())
