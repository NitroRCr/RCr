class UnicodeFont:
    styles = {
        'letters': {
            'normal': 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
            'bold': '𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙',
            'italic': '𝑎𝑏𝑐𝑑𝑒𝑓𝑔𝑕𝑖𝑗𝑘𝑙𝑚𝑛𝑜𝑝𝑞𝑟𝑠𝑡𝑢𝑣𝑤𝑥𝑦𝑧𝐴𝐵𝐶𝐷𝐸𝐹𝐺𝐻𝐼𝐽𝐾𝐿𝑀𝑁𝑂𝑃𝑄𝑅𝑆𝑇𝑈𝑉𝑊𝑋𝑌𝑍',
            'monospace': '𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉',
            'script': '𝒶𝒷𝒸𝒹𝑒𝒻𝑔𝒽𝒾𝒿𝓀𝓁𝓂𝓃𝑜𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏𝒜𝐵𝒞𝒟𝐸𝐹𝒢𝐻𝐼𝒥𝒦𝐿𝑀𝒩𝒪𝒫𝒬𝑅𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵',
            'bold-italic': '𝒂𝒃𝒄𝒅𝒆𝒇𝒈𝒉𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒒𝒓𝒔𝒕𝒖𝒗𝒘𝒙𝒚𝒛𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁',
            'bold-script': '𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩',
            'double-struck': '𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ',
            'sans-serif': '𝖺𝖻𝖼𝖽𝖾𝖿𝗀𝗁𝗂𝗃𝗄𝗅𝗆𝗇𝗈𝗉𝗊𝗋𝗌𝗍𝗎𝗏𝗐𝗑𝗒𝗓𝖠𝖡𝖢𝖣𝖤𝖥𝖦𝖧𝖨𝖩𝖪𝖫𝖬𝖭𝖮𝖯𝖰𝖱𝖲𝖳𝖴𝖵𝖶𝖷𝖸𝖹',
            'sans-serif-bold': '𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭',
            'sans-serif-italic': '𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡',
            'sans-serif-bold-italic': '𝙖𝙗𝙘𝙙𝙚𝙛𝙜𝙝𝙞𝙟𝙠𝙡𝙢𝙣𝙤𝙥𝙦𝙧𝙨𝙩𝙪𝙫𝙬𝙭𝙮𝙯𝘼𝘽𝘾𝘿𝙀𝙁𝙂𝙃𝙄𝙅𝙆𝙇𝙈𝙉𝙊𝙋𝙌𝙍𝙎𝙏𝙐𝙑𝙒𝙓𝙔𝙕',
            'reverse': 'ɐqɔpǝɟƃɥᴉɾʞlɯuodbɹsʇnʌʍxʎzⱯꓭƆꓷꓱℲꓨHIꓩꞰꓶꟽNOꓒQꓤSꞱꓵɅMX⅄Z',
        },
        'numbers': {
            'normal': '0123456789',
            'bold': '𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗',
            'monospace': '𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿',
            'sans-serif': '𝟢𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫',
            'double-struck': '𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡',
            'sans-serif-bold': '𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵',
        },
        'marks': {
            'normal': ['?', '.', ',', '!', '&', '"'],
            'reverse': ['¿', '˙', "'", '¡', '⅋', ',,'],
        },
    }
    style_name_list = [
        'bold',
        'italic',
        'monospace',
        'script',
        'bold-script',
        'bold-italic',
        'double-struck',
        'sans-serif',
        'sans-serif-bold',
        'sans-serif-italic',
        'sans-serif-bold-italic',
        'reverse'
    ]

    # 批量替换
    def replace_all(self, text, to_, from_):
        if len(from_) != len(to_):
            print(from_, to_)
            raise ValueError("参数长度不一致")
        result = ''
        for i in text:
            found = False
            for j in range(len(from_)):
                if i == from_[j]:
                    result += to_[j]
                    found = True
            if not found:
                result += i
        return result

    # 将text转换为指定字体的字符串并返回
    def font(self, text, to_, from_='normal'):
        for i in self.styles:
            group = self.styles[i]
            if not (from_ in group and to_ in group):
                continue
            text = self.replace_all(text, group[to_], group[from_])
        return text

    # 返回text的所有字体形式
    def all_fonts(self, text):
        result = {}
        for i in self.style_name_list:
            result[i] = (self.font(text, i))
        return result


def main():
    uf = UnicodeFont()
    print('''UnicodeFont
a.字体转换
b.使用说明
c.退出
d.常见问题
''')
    choice = input().lower()
    if choice == 'a':
        text = input('输入任意英文：')
        result = uf.all_fonts(text)
        print('\nResult:\n')
        for i in result:
            print('%s: %s' % (i, result[i]))
        print('\n')
        input('输入任意字符返回主页')
        main()
    elif choice == 'b':
        example = uf.all_fonts('Example Text, 01234.')
        print('''
UnicodeFont
这是一个文本处理工具，赋予文本更多的样式
它可以将任意英文，转换为几种不同的字体样式。然后复制粘贴到各种地方使用
它通过使用MATHEMATICAL字符集，将每个拉丁文字母替换为相应字体的字符，从文本上直接改变了字体
因此，它在很多地方通用。在任何完整支持Unicode且字体支持的地方都能够正常显示
比如，可以将转换后的文本粘贴到微信、微博等，发布后其他人也能看到字体效果
注：需要当前环境的字体支持，字体样式才能正常显示，否则会乱码
样式预览：
''')
        for i in example:
            print('%s: %s' % (i, example[i]))
        print('\n')
        input('输入任意字符返回主页')
        main()
    elif choice == 'c':
        print('Bye!')
        return
    elif choice == 'd':
        print('''
乱码问题：
    输出文本无法正常显示的问题，如下列文本：
    𝙃𝙚𝙡𝙡𝙤 𝙬𝙤𝙧𝙡𝙙
    正常显示为粗斜体
    如果有乱码，则是当前环境的字体不支持。
    
解决方法：
    1.使用字体支持的IDE或终端运行
    2.或者直接复制显示为乱码的文本，粘贴到其他字体支持的地方，仍然可以正常使用
''')
        input('输入任意字符返回主页')
        main()
    else:
        print('无效输入\n')
        main()


main()
