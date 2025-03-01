from akaiafiuk.rectangle_area import house_area


def test_house_area():
    assert house_area('''
                  0000000
                  ##00##0
                  ######0
                  ##00##0
                  #0000#0
        ''') == 24
    assert house_area('''
            0##0
            0000
            #00#
            ''') == 12
