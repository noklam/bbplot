def bbc_theme():
    # Typography
    font = "Lato"
    # At Urban it's the same font for all text but it's good to keep them separate in case you want to change one later.
    labelFont = "Lato"
    sourceFont = "Lato"
    labelFontSize = 18
    # Axes
    axisColor = "#000000"
    gridColor = "#DEDDDD"
    # Colors
    main_palette = [
        "#1696d2",
        "#d2d2d2",
        "#000000",
        "#fdbf11",
        "#ec008b",
        "#55b748",
        "#5c5859",
        "#db2b27",
    ]
    sequential_palette = [
        "#cfe8f3",
        "#a2d4ec",
        "#73bfe2",
        "#46abdb",
        "#1696d2",
        "#12719e",
    ]
    return {
        # width and height are configured outside the config dict because they are Chart configurations/properties not chart-elements' configurations/properties.
        # "width": 512,  # from the guide
        # "height": 288,  # not in the guide
        "width": 650, # from the guide
        "height": 450, # not in the guide
        "config": {
            "title": {
                "fontSize": 28,
                "font": font,
                "anchor": "start",  # equivalent of left-aligned.
                "fontColor": "#000000",
                # "text": "Title",
                # 'subtitle':'Subtitle',
                "subtitleFontSize": 18,
            },
            "axisX": {
                "domain": True,
                "domainColor": axisColor,
                "domainWidth": 1,
                "grid": False,
                "labelFont": labelFont,
                "labelFontSize": labelFontSize,
                "labelAngle": 0,
                "labelPadding": 10,
                "tickColor": axisColor,
                "tickSize": 5,  # default, including it just to show you can change it
                "titleFont": font,
                "titleFontSize": labelFontSize,
                "titlePadding": 10,  # guessing, not specified in styleguide
            },
            "axisY": {
                "domain": False,
                "grid": True,
                "gridColor": gridColor,
                "gridWidth": 1,
                "labelFont": labelFont,
                "labelFontSize": labelFontSize,
                "labelAngle": 0,
                "labelPadding": 10,
                "ticks": False,  # even if you don't have a "domain" you need to turn these off.
                "titleFont": font,
                "titleFontSize": labelFontSize,
                "titlePadding": 10,  # guessing, not specified in styleguide
                # titles are by default vertical left of axis so we need to hack this
                "titleAngle": 0,  # horizontal
                "titleY": -11,  # move it up
                "titleX": -3,  # move it to the right so it aligns with the labels
            },
                  "header": {
                "labelFontSize": 18,
                "titleFontSize": 18,
            },
            "range": {"category": main_palette, "diverging": sequential_palette,},
            "legend": {
                "labelFont": labelFont,
                "labelFontSize": labelFontSize,
                "symbolType": "square",  # just 'cause
                "symbolSize": 100,  # default
                "titleFont": font,
                "titleFontSize": labelFontSize,
                "title": "",  # set it to no-title by default
                "orient": "top-left",  # so it's right next to the y-axis
                "offset": 0,  # literally right next to the y-axis.
            },
            "view": {
                "stroke": "transparent",  # altair uses gridlines to box the area where the data is visualized. This takes that off.
            },
            # "background":{
            #     "color":'#FFFFFF'
            # },
            ## MARKS CONFIGURATIONS ###
            # "area": {
            #     #    "fill": markColor,
            # },
            # # "line": {
            #        "color": "#FFFFFF",
            #        "stroke": "#FFFFFF",
            #     "strokeWidth": 5,
            # },
            # "trail": {
            #     #    "color": markColor,
            #     #    "stroke": markColor,
            #     "strokeWidth": 0,
            #     "size": 1,
            # },
            # "path": {
            #     #    "stroke": markColor,
            #     "strokeWidth": 0.5,
            # },
            # "point": {"filled": True,},
            # "text": {
            #     "font": sourceFont,
            #     #    "color": markColor,
            #     "fontSize": 11,
            #     "align": "right",
            #     #    "fontWeight": 400,
            #     "size": 11,
            # },
            # "bar": {
            #     "size": 40,
            #     "binSpacing": 1,
            #     "continuousBandSize": 30,
            #     "discreteBandSize": 30,
            #     # "fill": markColor,
            #     "stroke": False,
            # },
        },
    }
