# Todo list

1. remove cleaner.py
2. remove rename.py
3. add this functionality to swisstool.py
4. add startswith functionality to swisstool
5. add endswith functionality to swisstool
6. Update roguelike
7. do MySQL work
8. do Django work
9. Build games
   1. snake
   2. tetris
   3. brick
   4. match
   5. roguelike
   6. wargame
10. fix linting issues
Run pylint --rcfile=pylint.rc $(git ls-files '*.py')
************* Module recoverdata
code/datarecovery/recoverdata.py:17:0: R0914: Too many local variables (24/15) (too-many-locals)
code/datarecovery/recoverdata.py:23:12: R1732: Consider using 'with' for resource-allocating operations (consider-using-with)
code/datarecovery/recoverdata.py:50:20: R1732: Consider using 'with' for resource-allocating operations (consider-using-with)
code/datarecovery/recoverdata.py:71:21: R1732: Consider using 'with' for resource-allocating operations (consider-using-with)
************* Module StrategyGameWithAIBeta14
code/game/StrategyGame/StrategyGameWithAIBeta14.py:239:0: R0914: Too many local variables (20/15) (too-many-locals)
code/game/StrategyGame/StrategyGameWithAIBeta14.py:269:4: R1702: Too many nested blocks (6/5) (too-many-nested-blocks)
code/game/StrategyGame/StrategyGameWithAIBeta14.py:269:4: R1702: Too many nested blocks (6/5) (too-many-nested-blocks)
code/game/StrategyGame/StrategyGameWithAIBeta14.py:269:4: R1702: Too many nested blocks (7/5) (too-many-nested-blocks)
************* Module TKBoid
code/game/TKBoid.py:39:18: W0613: Unused argument 'event' (unused-argument)
code/game/TKBoid.py:42:18: W0613: Unused argument 'event' (unused-argument)
code/game/TKBoid.py:104:0: R0901: Too many ancestors (9/7) (too-many-ancestors)
code/game/TKBoid.py:260:25: W0613: Unused argument 'group' (unused-argument)
code/game/TKBoid.py:292:4: R0914: Too many local variables (17/15) (too-many-locals)
code/game/TKBoid.py:188:12: W0201: Attribute 'palette' defined outside __init__ (attribute-defined-outside-init)
code/game/TKBoid.py:218:12: W0201: Attribute 'target' defined outside __init__ (attribute-defined-outside-init)
code/game/TKBoid.py:435:30: W0613: Unused argument 'group' (unused-argument)
code/game/TKBoid.py:205:20: W0201: Attribute 'color' defined outside __init__ (attribute-defined-outside-init)
code/game/TKBoid.py:207:20: W0201: Attribute 'color' defined outside __init__ (attribute-defined-outside-init)
************* Module ai
code/game/conquer/ai.py:39:4: R0914: Too many local variables (24/15) (too-many-locals)
code/game/conquer/ai.py:83:28: R1714: Consider merging these comparisons with "in" to 'pala2 not in (self.board.turn, 0)' (consider-using-in)
code/game/conquer/ai.py:49:8: R1702: Too many nested blocks (8/5) (too-many-nested-blocks)
code/game/conquer/ai.py:49:8: R1702: Too many nested blocks (8/5) (too-many-nested-blocks)
************* Module classcollection
code/game/conquer/classcollection.py:69:8: R1702: Too many nested blocks (6/5) (too-many-nested-blocks)
code/game/conquer/classcollection.py:69:8: R1702: Too many nested blocks (6/5) (too-many-nested-blocks)
code/game/conquer/classcollection.py:93:24: W0201: Attribute 'turn' defined outside __init__ (attribute-defined-outside-init)
************* Module gameboard
code/game/conquer/gameboard.py:1:0: C0302: Too many lines in module (1564/1000) (too-many-lines)
code/game/conquer/gameboard.py:30:0: W0401: Wildcard import classcollection (wildcard-import)
code/game/conquer/gameboard.py:31:0: W0401: Wildcard import recurser (wildcard-import)
code/game/conquer/gameboard.py:32:0: W0401: Wildcard import ai (wildcard-import)
code/game/conquer/gameboard.py:228:8: R1702: Too many nested blocks (6/5) (too-many-nested-blocks)
code/game/conquer/gameboard.py:228:8: R1702: Too many nested blocks (6/5) (too-many-nested-blocks)
code/game/conquer/gameboard.py:308:47: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
code/game/conquer/gameboard.py:310:47: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
code/game/conquer/gameboard.py:441:24: W0613: Unused argument 'y' (unused-argument)
code/game/conquer/gameboard.py:520:4: R0911: Too many return statements (7/6) (too-many-return-statements)
code/game/conquer/gameboard.py:618:8: R1702: Too many nested blocks (6/5) (too-many-nested-blocks)
code/game/conquer/gameboard.py:753:33: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
code/game/conquer/gameboard.py:755:33: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
code/game/conquer/gameboard.py:763:42: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
code/game/conquer/gameboard.py:766:25: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
code/game/conquer/gameboard.py:786:8: W0702: No exception type(s) specified (bare-except)
code/game/conquer/gameboard.py:780:33: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
code/game/conquer/gameboard.py:784:33: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
code/game/conquer/gameboard.py:794:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
code/game/conquer/gameboard.py:809:25: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
code/game/conquer/gameboard.py:813:25: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
code/game/conquer/gameboard.py:823:25: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
code/game/conquer/gameboard.py:826:25: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
code/game/conquer/gameboard.py:830:29: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
code/game/conquer/gameboard.py:869:45: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
code/game/conquer/gameboard.py:873:37: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
code/game/conquer/gameboard.py:847:8: R1702: Too many nested blocks (6/5) (too-many-nested-blocks)
code/game/conquer/gameboard.py:891:25: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
code/game/conquer/gameboard.py:892:25: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
code/game/conquer/gameboard.py:893:25: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
code/game/conquer/gameboard.py:906:12: W0702: No exception type(s) specified (bare-except)
code/game/conquer/gameboard.py:923:16: W0702: No exception type(s) specified (bare-except)
code/game/conquer/gameboard.py:922:52: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
code/game/conquer/gameboard.py:980:8: R1702: Too many nested blocks (7/5) (too-many-nested-blocks)
code/game/conquer/gameboard.py:932:4: R0911: Too many return statements (10/6) (too-many-return-statements)
code/game/conquer/gameboard.py:980:8: R1702: Too many nested blocks (7/5) (too-many-nested-blocks)
code/game/conquer/gameboard.py:1021:4: R0914: Too many local variables (28/15) (too-many-locals)
code/game/conquer/gameboard.py:1029:8: R1702: Too many nested blocks (6/5) (too-many-nested-blocks)
code/game/conquer/gameboard.py:1029:8: R1702: Too many nested blocks (6/5) (too-many-nested-blocks)
code/game/conquer/gameboard.py:1029:8: R1702: Too many nested blocks (9/5) (too-many-nested-blocks)
code/game/conquer/gameboard.py:1029:8: R1702: Too many nested blocks (8/5) (too-many-nested-blocks)
code/game/conquer/gameboard.py:1029:8: R1702: Too many nested blocks (6/5) (too-many-nested-blocks)
code/game/conquer/gameboard.py:1029:8: R1702: Too many nested blocks (7/5) (too-many-nested-blocks)
code/game/conquer/gameboard.py:1197:8: R1702: Too many nested blocks (9/5) (too-many-nested-blocks)
code/game/conquer/gameboard.py:1197:8: R1702: Too many nested blocks (6/5) (too-many-nested-blocks)
code/game/conquer/gameboard.py:1270:8: W0702: No exception type(s) specified (bare-except)
code/game/conquer/gameboard.py:1256:63: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
code/game/conquer/gameboard.py:1261:63: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
code/game/conquer/gameboard.py:1492:25: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
code/game/conquer/gameboard.py:1489:8: R1702: Too many nested blocks (6/5) (too-many-nested-blocks)
code/game/conquer/gameboard.py:65:0: R0904: Too many public methods (48/20) (too-many-public-methods)
code/game/conquer/gameboard.py:30:0: W0614: Unused import(s) TIH, sep and path from wildcard import of classcollection (unused-wildcard-import)
************* Module gamemenu
code/game/conquer/gamemenu.py:127:14: R0133: Comparison between constants: '1 != 0' has a constant value (comparison-of-constants)
code/game/conquer/gamemenu.py:151:99: W0613: Unused argument 'keskita' (unused-argument)
************* Module hex
code/game/hex.py:9:0: R0914: Too many local variables (17/15) (too-many-locals)
************* Module qq
code/game/thesheep/qq.py:21:0: E0401: Unable to import 'ConfigParser' (import-error)
code/game/thesheep/qq.py:34:0: R0205: Class 'TileCache' inherits from object, can be safely removed from bases in python3 (useless-object-inheritance)
code/game/thesheep/qq.py:34:0: R0903: Too few public methods (1/2) (too-few-public-methods)
code/game/thesheep/qq.py:69:0: R0903: Too few public methods (1/2) (too-few-public-methods)
code/game/thesheep/qq.py:88:0: W0613: Unused argument 'args' (unused-argument)
code/game/thesheep/qq.py:78:0: R0903: Too few public methods (1/2) (too-few-public-methods)
code/game/thesheep/qq.py:100:8: R1725: Consider using Python 3 style super() without arguments (super-with-arguments)
code/game/thesheep/qq.py:137:0: W0613: Unused argument 'args' (unused-argument)
code/game/thesheep/qq.py:117:8: W0201: Attribute 'depth' defined outside __init__ (attribute-defined-outside-init)
code/game/thesheep/qq.py:125:8: W0201: Attribute 'depth' defined outside __init__ (attribute-defined-outside-init)
code/game/thesheep/qq.py:177:0: R0205: Class 'Level' inherits from object, can be safely removed from bases in python3 (useless-object-inheritance)
code/game/thesheep/qq.py:290:0: R0205: Class 'Game' inherits from object, can be safely removed from bases in python3 (useless-object-inheritance)
************* Module examplemysql
code/mysqlpython/examplemysql.py:41:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
************* Module insta
code/social/insta.py:72:7: E0602: Undefined variable 'ClientError' (undefined-variable)
************* Module tktest
code/tkfolder/tktest.py:7:0: W0212: Access to a protected member _test of a client class (protected-access)
************* Module tktodo
code/tkfolder/tktodo.py:5:20: C0303: Trailing whitespace (trailing-whitespace)
************* Module movetype
code/utilities/movetype.py:6:38: R1732: Consider using 'with' for resource-allocating operations (consider-using-with)
************* Module crawler
code/web/crawler.py:139:8: R1702: Too many nested blocks (6/5) (too-many-nested-blocks)
code/web/crawler.py:206:22: R1732: Consider using 'with' for resource-allocating operations (consider-using-with)

************* Module ISBN
scratch/ISBN.py:62:18: W1401: Anomalous backslash in string: '\W'. String constant might be missing an r prefix. (anomalous-backslash-in-string)
scratch/ISBN.py:63:19: W1401: Anomalous backslash in string: '\D'. String constant might be missing an r prefix. (anomalous-backslash-in-string)
scratch/ISBN.py:71:8: E0702: Raising str while only classes or instances are allowed (raising-bad-type)
scratch/ISBN.py:78:4: E0702: Raising str while only classes or instances are allowed (raising-bad-type)
scratch/ISBN.py:184:8: E0702: Raising str while only classes or instances are allowed (raising-bad-type)
scratch/ISBN.py:194:8: E0702: Raising str while only classes or instances are allowed (raising-bad-type)

-----------------------------------
Your code has been rated at 9.83/10
