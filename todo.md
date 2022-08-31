<<<<<<< Updated upstream
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
=======
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
************* Module StrategyGameWithAIBeta14
code/game/StrategyGame/StrategyGameWithAIBeta14.py:239:0: R0914: Too many local variables (20/15) (too-many-locals)
code/game/StrategyGame/StrategyGameWithAIBeta14.py:269:4: R1702: Too many nested blocks (6/5) (too-many-nested-blocks)
code/game/StrategyGame/StrategyGameWithAIBeta14.py:269:4: R1702: Too many nested blocks (6/5) (too-many-nested-blocks)
code/game/StrategyGame/StrategyGameWithAIBeta14.py:269:4: R1702: Too many nested blocks (7/5) (too-many-nested-blocks)
************* Module ai
code/game/conquer/ai.py:35:21: E0001: inconsistent use of tabs and spaces in indentation (<unknown>, line 35) (syntax-error)
************* Module classcollection
code/game/conquer/classcollection.py:148:31: E0001: inconsistent use of tabs and spaces in indentation (<unknown>, line 148) (syntax-error)
************* Module conquer
code/game/conquer/conquer.py:87:0: W0311: Bad indentation. Found 1 spaces, expected 4 (bad-indentation)
code/game/conquer/conquer.py:89:0: W0311: Bad indentation. Found 1 spaces, expected 4 (bad-indentation)
code/game/conquer/conquer.py:92:0: W0311: Bad indentation. Found 1 spaces, expected 4 (bad-indentation)
code/game/conquer/conquer.py:115:0: W0311: Bad indentation. Found 1 spaces, expected 4 (bad-indentation)
code/game/conquer/conquer.py:116:0: W0311: Bad indentation. Found 1 spaces, expected 4 (bad-indentation)
code/game/conquer/conquer.py:121:0: W0311: Bad indentation. Found 2 spaces, expected 8 (bad-indentation)
code/game/conquer/conquer.py:123:0: W0311: Bad indentation. Found 2 spaces, expected 8 (bad-indentation)
code/game/conquer/conquer.py:126:0: W0311: Bad indentation. Found 2 spaces, expected 8 (bad-indentation)
code/game/conquer/conquer.py:129:0: W0311: Bad indentation. Found 2 spaces, expected 8 (bad-indentation)
code/game/conquer/conquer.py:130:0: W0311: Bad indentation. Found 3 spaces, expected 12 (bad-indentation)
code/game/conquer/conquer.py:133:0: W0311: Bad indentation. Found 2 spaces, expected 8 (bad-indentation)
code/game/conquer/conquer.py:137:0: W0311: Bad indentation. Found 2 spaces, expected 8 (bad-indentation)
code/game/conquer/conquer.py:138:0: W0311: Bad indentation. Found 2 spaces, expected 8 (bad-indentation)
code/game/conquer/conquer.py:140:0: W0311: Bad indentation. Found 3 spaces, expected 12 (bad-indentation)
code/game/conquer/conquer.py:141:0: W0311: Bad indentation. Found 3 spaces, expected 12 (bad-indentation)
code/game/conquer/conquer.py:142:0: W0311: Bad indentation. Found 3 spaces, expected 12 (bad-indentation)
code/game/conquer/conquer.py:145:0: W0311: Bad indentation. Found 1 spaces, expected 4 (bad-indentation)
code/game/conquer/conquer.py:147:0: W0311: Bad indentation. Found 2 spaces, expected 8 (bad-indentation)
code/game/conquer/conquer.py:148:0: W0311: Bad indentation. Found 2 spaces, expected 8 (bad-indentation)
code/game/conquer/conquer.py:151:0: W0311: Bad indentation. Found 2 spaces, expected 8 (bad-indentation)
code/game/conquer/conquer.py:154:0: W0311: Bad indentation. Found 2 spaces, expected 8 (bad-indentation)
code/game/conquer/conquer.py:157:0: W0311: Bad indentation. Found 1 spaces, expected 4 (bad-indentation)
code/game/conquer/conquer.py:158:0: W0311: Bad indentation. Found 2 spaces, expected 8 (bad-indentation)
code/game/conquer/conquer.py:161:0: W0311: Bad indentation. Found 3 spaces, expected 12 (bad-indentation)
code/game/conquer/conquer.py:162:0: W0311: Bad indentation. Found 3 spaces, expected 12 (bad-indentation)
code/game/conquer/conquer.py:163:0: W0311: Bad indentation. Found 4 spaces, expected 16 (bad-indentation)
code/game/conquer/conquer.py:166:0: W0311: Bad indentation. Found 1 spaces, expected 4 (bad-indentation)
code/game/conquer/conquer.py:169:0: W0311: Bad indentation. Found 2 spaces, expected 8 (bad-indentation)
code/game/conquer/conquer.py:172:0: W0311: Bad indentation. Found 2 spaces, expected 8 (bad-indentation)
code/game/conquer/conquer.py:175:0: W0311: Bad indentation. Found 2 spaces, expected 8 (bad-indentation)
code/game/conquer/conquer.py:176:0: W0311: Bad indentation. Found 2 spaces, expected 8 (bad-indentation)
code/game/conquer/conquer.py:177:0: W0311: Bad indentation. Found 2 spaces, expected 8 (bad-indentation)
code/game/conquer/conquer.py:178:0: W0311: Bad indentation. Found 2 spaces, expected 8 (bad-indentation)
code/game/conquer/conquer.py:181:0: W0311: Bad indentation. Found 2 spaces, expected 8 (bad-indentation)
code/game/conquer/conquer.py:184:0: W0311: Bad indentation. Found 2 spaces, expected 8 (bad-indentation)
code/game/conquer/conquer.py:185:0: W0311: Bad indentation. Found 2 spaces, expected 8 (bad-indentation)
code/game/conquer/conquer.py:188:0: W0311: Bad indentation. Found 1 spaces, expected 4 (bad-indentation)
code/game/conquer/conquer.py:189:0: W0311: Bad indentation. Found 2 spaces, expected 8 (bad-indentation)
code/game/conquer/conquer.py:167:3: W0511: FIXME: little better looking (fixme)
code/game/conquer/conquer.py:1:0: C0114: Missing module docstring (missing-module-docstring)
code/game/conquer/conquer.py:33:0: E0001: Cannot import 'classcollection' due to syntax error 'inconsistent use of tabs and spaces in indentation (<unknown>, line 148)' (syntax-error)
code/game/conquer/conquer.py:47:0: E0001: Cannot import 'gameboard' due to syntax error 'invalid syntax (<unknown>, line 360)' (syntax-error)
code/game/conquer/conquer.py:47:0: C0413: Import "import gameboard" should be placed at the top of the module (wrong-import-position)
code/game/conquer/conquer.py:48:0: E0001: Cannot import 'gameboard' due to syntax error 'invalid syntax (<unknown>, line 360)' (syntax-error)
code/game/conquer/conquer.py:48:0: C0413: Import "from gameboard import TGB" should be placed at the top of the module (wrong-import-position)
code/game/conquer/conquer.py:49:0: E0001: Cannot import 'gamemenu' due to syntax error 'invalid syntax (<unknown>, line 25)' (syntax-error)
code/game/conquer/conquer.py:49:0: C0413: Import "import gamemenu" should be placed at the top of the module (wrong-import-position)
code/game/conquer/conquer.py:58:0: C0103: Constant name "conquer_version" doesn't conform to UPPER_CASE naming style (invalid-name)
code/game/conquer/conquer.py:112:0: C0103: Constant name "main_loop_running" doesn't conform to UPPER_CASE naming style (invalid-name)
code/game/conquer/conquer.py:189:2: C0103: Constant name "main_loop_running" doesn't conform to UPPER_CASE naming style (invalid-name)
************* Module gameboard
code/game/conquer/gameboard.py:360:31: E0001: invalid syntax (<unknown>, line 360) (syntax-error)
************* Module gamemenu
code/game/conquer/gamemenu.py:25:52: E0001: invalid syntax (<unknown>, line 25) (syntax-error)
************* Module hex_system
code/game/conquer/hex_system.py:1:0: C0114: Missing module docstring (missing-module-docstring)
************* Module recurser
code/game/conquer/recurser.py:68:10: E0001: Missing parentheses in call to 'print'. Did you mean print("World area: %d" % land_area)? (<unknown>, line 68) (syntax-error)
************* Module conf
code/game/thesheep/docs/conf.py:1:0: C0114: Missing module docstring (missing-module-docstring)
code/game/thesheep/docs/conf.py:44:0: W0622: Redefining built-in 'copyright' (redefined-builtin)
code/game/thesheep/docs/conf.py:14:0: C0410: Multiple imports on one line (sys, os) (multiple-imports)
code/game/thesheep/docs/conf.py:34:0: C0103: Constant name "source_suffix" doesn't conform to UPPER_CASE naming style (invalid-name)
code/game/thesheep/docs/conf.py:40:0: C0103: Constant name "master_doc" doesn't conform to UPPER_CASE naming style (invalid-name)
code/game/thesheep/docs/conf.py:43:0: C0103: Constant name "project" doesn't conform to UPPER_CASE naming style (invalid-name)
code/game/thesheep/docs/conf.py:43:10: W1406: The u prefix for strings is no longer necessary in Python >=3.0 (redundant-u-string-prefix)
code/game/thesheep/docs/conf.py:44:0: C0103: Constant name "copyright" doesn't conform to UPPER_CASE naming style (invalid-name)
>>>>>>> Stashed changes
