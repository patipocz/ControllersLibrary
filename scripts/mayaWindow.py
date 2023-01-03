import maya.cmds as cmds

# create the basic UI for the controllers library, to be replacedd with a nice proper QT window

# from ControllersLibrary import functions
import functions


def controllersLibWindow():
    def circleButtonPush(*args):
        circleName = cmds.textField("circleNameField", q=True, tx=True)
        circleRadius = cmds.floatField("circleRadiusFloatField", q=True, v=True)
        print(circleName, circleRadius)
        functions.createCircleCtrl(circleCtrlName=circleName, radius=circleRadius)
        # print(circleCtrlName)
        # cmds.group(name=finalCircleController+"_offset")

    def lolliButtonPush(*args):
        lolliName = cmds.textField("lollipopNameField", q=True, tx=True)
        lolliRadius = cmds.floatField("lolliRadiusFloatField", q=True, v=True)
        verticalCircles = cmds.intField("verticalCirclesIntField", q=True, v=True)
        horizontalCircles = cmds.intField("horizontalCirclesIntField", q=True, v=True)
        lolliStickLength = cmds.floatField("lolliStickLengthFloatField", q=True, v=True)
        print(lolliName, lolliRadius, verticalCircles)
        functions.createLollipopCtrl(
            lollipopCtrlName=lolliName,
            radiusLolli=lolliRadius,
            numberOfVerticalCircles=verticalCircles,
            numberOfHorizontalCircles=horizontalCircles,
            stickLength=lolliStickLength,
        )

    def rectangleButtonPush(*args):
        rectCtrlName = cmds.textField("rectangleNameField", q=True, tx=True)
        rectCtrlWidth = cmds.floatField("recWidthFloatField", q=True, v=True)
        rectCtrlHeight = cmds.floatField("recHeightFloatField", q=True, v=True)
        print(rectCtrlName, rectCtrlWidth)
        functions.createRectangleCtrl(
            rectangleCtrlName=rectCtrlName,
            rectangleWidth=rectCtrlWidth,
            rectangleHeight=rectCtrlHeight,
        )

    def squareLolliButtonPush(*args):
        squareLolliNameInput = cmds.textField("squareLolliNameField", q=True, tx=True)
        squareLolliSide = cmds.floatField("sqLolliSideLengthFloatField", q=True, v=True)
        squareLolliStickLengthInput = cmds.floatField(
            "sqLolliStickLengthFloatField", q=True, v=True
        )
        functions.createSquareLolliCtrl(
            squareLolliCtrlName=squareLolliNameInput,
            squareSide=squareLolliSide,
            stickLength=squareLolliStickLengthInput,
        )

    def fkikButtonPush(*args):
        functions.createFKIKSwitchCtrl()

    def customTxtButtonPush(*args):
        customTxtName = cmds.textField("customTxtNameField", q=True, tx=True)
        customTxtUsrInput = cmds.textField("inputTextField", q=True, tx=True)
        customTxtFont = cmds.textField("fontField", q=True, tx=True)
        functions.createCustomTextCtrl(
            customTextCtrlName=customTxtName,
            customTextInput=customTxtUsrInput,
            chooseFont=customTxtFont,
        )

    def groupCtrlButtonPush(*args):
        functions.groupCtrl()

    # WINDOW

    cmds.window(title="Controllers Library", iconName="CtrlLib", widthHeight=(600, 620))
    cmds.columnLayout(adjustableColumn=True)

    # cmds.text(label='Controllers')
    # cmds.separator()
    # cmds.separator()

    # CIRCULAR CONTROLLERS
    cmds.separator()
    cmds.frameLayout(
        label="Circular Controllers",
        collapsable=True,
        labelAlign="top",
        borderStyle="in",
    )

    cmds.paneLayout(configuration="vertical2")
    # left
    cmds.columnLayout(adjustableColumn=True)
    cmds.text(label="Circle Controller")
    cmds.separator()

    # cmds.rowLayout(numberOfColumns=2)
    # cmds.text(label='Radius')
    # cmds.floatField("radiusFloatField", value=10, minValue=0.1)
    # cmds.text(label='controller name'
    # cmds.textField()

    cmds.rowColumnLayout(
        numberOfColumns=2,
        columnAttach=(1, "right", 0),
        columnWidth=[(1, 150), (2, 130)],
    )
    cmds.text(label="Circle Ctrl Name")
    circNameTest = cmds.textField("circleNameField", tx="circleCtrl_001")
    cmds.text(label="Circle Radius")
    cmds.floatField("circleRadiusFloatField", value=5, minValue=0.1)

    cmds.setParent("..")  # back to column layout

    cmds.iconTextButton(
        style="iconAndTextHorizontal",
        image1="circleicon.png",
        label="Create Circle Controller",
        bgc=[0.5, 0.5, 0.5],
        command=circleButtonPush,
    )
    # cmds.button(label='Create Circle Controller')
    cmds.setParent("..")  # back to pane layout

    # right
    cmds.columnLayout(adjustableColumn=True)
    cmds.text(label="Lollipop Controller")
    cmds.separator()

    cmds.rowColumnLayout(
        numberOfColumns=2,
        columnAttach=(1, "right", 0),
        columnWidth=[(1, 150), (2, 130)],
    )
    cmds.text(label="Lollipop Ctrl Name")
    lolliNameTest = cmds.textField("lollipopNameField", tx="lollipopCtrl_001")
    cmds.text(label="Lolli Radius")
    cmds.floatField("lolliRadiusFloatField", value=2, minValue=0.1)
    cmds.text(label="No. of Vertical Circles")
    cmds.intField("verticalCirclesIntField", value=2, minValue=0)
    cmds.text(label="No. of Horizontal Circles")
    cmds.intField("horizontalCirclesIntField", value=1, minValue=0)
    cmds.text(label="Lolli Stick Length")
    lolliStickLengthInput = cmds.floatField(
        "lolliStickLengthFloatField", value=10, minValue=0)

    cmds.setParent("..")  # back to column layout

    cmds.iconTextButton(
        style="iconAndTextHorizontal",
        image1="lolliicon.png",
        label="Create Lollipop Controller",
        bgc=[0.5, 0.5, 0.5],
        command=lolliButtonPush,
    )
    # cmds.button(label='Create Lollipop Controller')

    cmds.setParent("..")  # back to pane layout
    cmds.setParent("..")  # back to frame layout
    cmds.setParent("..")  # back to main window column layout

    # RECTANGULAR CONTROLLERS
    cmds.separator()
    cmds.frameLayout(
        label="Rectangular Controllers",
        collapsable=True,
        labelAlign="top",
        borderStyle="in",
    )
    cmds.paneLayout(configuration="vertical2")
    # left
    cmds.columnLayout(adjustableColumn=True)
    cmds.text(label="Rectangular Controller")
    cmds.separator()

    cmds.rowColumnLayout(
        numberOfColumns=2,
        columnAttach=(1, "right", 0),
        columnWidth=[(1, 150), (2, 130)],
    )
    cmds.text(label="Rectangle Ctrl Name")
    rectName = cmds.textField("rectangleNameField", tx="rectangleCtrl_001")
    cmds.text(label="Width")
    recWidthInput = cmds.floatField("recWidthFloatField", value=6, minValue=0.1)
    cmds.text(label="Height")
    recHeightInput = cmds.floatField("recHeightFloatField", value=3, minValue=0.1)
    cmds.setParent("..")  # back to column layout

    cmds.iconTextButton(
        style="iconAndTextHorizontal",
        image1="sqricon.png",
        i="iconOnly",
        label="Create Rectangular Controller",
        bgc=[0.5, 0.5, 0.5],
        command=rectangleButtonPush,
    )
    # cmds.button(label='Create Rectangle Controller')
    cmds.setParent("..")  # back to pane layout

    # right
    cmds.columnLayout(adjustableColumn=True)
    cmds.text(label="Square Lollipop Controller")
    cmds.separator()
    cmds.rowColumnLayout(
        numberOfColumns=2,
        columnAttach=(1, "right", 0),
        columnWidth=[(1, 150), (2, 130)],
    )
    cmds.text(label="Square Lollipop Ctrl Name")
    squareLolliNameTextField = cmds.textField(
        "squareLolliNameField", tx="squareLolliCtrl_001"
    )
    cmds.text(label="Square Side Length")
    cmds.floatField("sqLolliSideLengthFloatField", value=3, minValue=0.1)
    cmds.text(label="Square Lolli Stick Length")
    cmds.floatField("sqLolliStickLengthFloatField", value=10, minValue=0)
    cmds.setParent("..")  # back to column layout
    cmds.iconTextButton(
        style="iconAndTextHorizontal",
        image1="sqrlolliicon.png",
        i="iconOnly",
        label="Create Square Lollipop Controller",
        bgc=[0.5, 0.5, 0.5],
        command=squareLolliButtonPush,
    )
    # cmds.button(label='Create Square Lolli Controller')

    cmds.setParent("..")  # back to pane layout
    cmds.setParent("..")  # back to column layout
    cmds.setParent("..")  # back to frame layout

    # OTHER CONTROLLERS
    cmds.separator()
    cmds.frameLayout(
        label="Other Controllers", collapsable=True, labelAlign="top", borderStyle="in")
    cmds.paneLayout(configuration="vertical2")
    # left
    cmds.columnLayout(adjustableColumn=True)
    cmds.text(label="FK/IK Switch Controller")
    cmds.separator()
    cmds.iconTextButton(
        style="iconAndTextHorizontal",
        image1="fkikicon.png",
        label="Create FK/IK Switch Controller",
        bgc=[0.5, 0.5, 0.5],
        command=fkikButtonPush,
    )
    # cmds.button(label='Create FK/IK Switch Controller')
    cmds.setParent("..")  # back to pane layout
    # right
    cmds.columnLayout(adjustableColumn=True)
    cmds.text(label="Custom Text Controller")
    cmds.separator()

    cmds.rowColumnLayout(
        numberOfColumns=2,
        columnAttach=(1, "right", 0),
        columnWidth=[(1, 150), (2, 130)],
    )
    cmds.text(label="Custom Txt Ctrl Name")
    txtNameField = cmds.textField("customTxtNameField", tx="customTextCtrl_001")
    cmds.text(label="Font")
    fontChoiceField = cmds.textField("fontField", tx="Arial")
    cmds.text(label="Text Input")
    customTxtField = cmds.textField("inputTextField", pht="input text")

    cmds.setParent("..")  # back to column layout

    cmds.iconTextButton(
        style="iconAndTextHorizontal",
        image1="customtxticon.png",
        label="Create Custom Text Controller",
        bgc=[0.5, 0.5, 0.5],
        command=customTxtButtonPush,
    )
    # cmds.button(label='Create Custom Text Controller')

    cmds.setParent("..")  # back to pane layout
    cmds.setParent("..")  # back to column layout
    cmds.setParent("..")  # back to frame layout

    cmds.columnLayout(adjustableColumn=True)
    cmds.separator()
    cmds.text(
        label="create an auto and offset group for the selected controllers, match pivots of their groups to the controller"
    )
    cmds.text(
        label="WARNING: Only run this after creation of all the controllers to avoid name clashes in the scene"
    )
    cmds.button(label="Create Auto Offset Grp", command=groupCtrlButtonPush)

    cmds.showWindow()
