# ScintillaConstants.py
# Define all the symbolic constants from Scintilla.iface so Python code can use them
# Copyright (c) 2011 Archaeopteryx Software, Inc. d/b/a Wingware

# ++Autogenerated -- start of section automatically generated from Scintilla.iface */
INVALID_POSITION=-1
SCI_START=2000
SCI_OPTIONAL_START=3000
SCI_LEXER_START=4000
SCI_ADDTEXT=2001
SCI_ADDSTYLEDTEXT=2002
SCI_INSERTTEXT=2003
SCI_CHANGEINSERTION=2672
SCI_CLEARALL=2004
SCI_DELETERANGE=2645
SCI_CLEARDOCUMENTSTYLE=2005
SCI_REDO=2011
SCI_SELECTALL=2013
SCI_SETSAVEPOINT=2014
SCI_GETSTYLEDTEXT=2015
SCI_CANREDO=2016
SCI_MARKERLINEFROMHANDLE=2017
SCI_MARKERDELETEHANDLE=2018
SCI_MARKERHANDLEFROMLINE=2732
SCI_MARKERNUMBERFROMLINE=2733
SCWS_INVISIBLE=0
SCWS_VISIBLEALWAYS=1
SCWS_VISIBLEAFTERINDENT=2
SCWS_VISIBLEONLYININDENT=3
SCTD_LONGARROW=0
SCTD_STRIKEOUT=1
SCI_POSITIONFROMPOINT=2022
SCI_POSITIONFROMPOINTCLOSE=2023
SCI_GOTOLINE=2024
SCI_GOTOPOS=2025
SCI_GETCURLINE=2027
SC_EOL_CRLF=0
SC_EOL_CR=1
SC_EOL_LF=2
SCI_CONVERTEOLS=2029
SCI_STARTSTYLING=2032
SCI_SETSTYLING=2033
SCI_CLEARTABSTOPS=2675
SCI_ADDTABSTOP=2676
SCI_GETNEXTTABSTOP=2677
SC_CP_UTF8=65001
SC_IME_WINDOWED=0
SC_IME_INLINE=1
SC_ALPHA_TRANSPARENT=0
SC_ALPHA_OPAQUE=255
SC_ALPHA_NOALPHA=256
SC_CURSORNORMAL=-1
SC_CURSORARROW=2
SC_CURSORWAIT=4
SC_CURSORREVERSEARROW=7
MARKER_MAX=31
SC_MARK_CIRCLE=0
SC_MARK_ROUNDRECT=1
SC_MARK_ARROW=2
SC_MARK_SMALLRECT=3
SC_MARK_SHORTARROW=4
SC_MARK_EMPTY=5
SC_MARK_ARROWDOWN=6
SC_MARK_MINUS=7
SC_MARK_PLUS=8
SC_MARK_VLINE=9
SC_MARK_LCORNER=10
SC_MARK_TCORNER=11
SC_MARK_BOXPLUS=12
SC_MARK_BOXPLUSCONNECTED=13
SC_MARK_BOXMINUS=14
SC_MARK_BOXMINUSCONNECTED=15
SC_MARK_LCORNERCURVE=16
SC_MARK_TCORNERCURVE=17
SC_MARK_CIRCLEPLUS=18
SC_MARK_CIRCLEPLUSCONNECTED=19
SC_MARK_CIRCLEMINUS=20
SC_MARK_CIRCLEMINUSCONNECTED=21
SC_MARK_BACKGROUND=22
SC_MARK_DOTDOTDOT=23
SC_MARK_ARROWS=24
SC_MARK_PIXMAP=25
SC_MARK_FULLRECT=26
SC_MARK_LEFTRECT=27
SC_MARK_AVAILABLE=28
SC_MARK_UNDERLINE=29
SC_MARK_RGBAIMAGE=30
SC_MARK_BOOKMARK=31
SC_MARK_VERTICALBOOKMARK=32
SC_MARK_CHARACTER=10000
SC_MARKNUM_FOLDEREND=25
SC_MARKNUM_FOLDEROPENMID=26
SC_MARKNUM_FOLDERMIDTAIL=27
SC_MARKNUM_FOLDERTAIL=28
SC_MARKNUM_FOLDERSUB=29
SC_MARKNUM_FOLDER=30
SC_MARKNUM_FOLDEROPEN=31
SC_MASK_FOLDERS=0xFE000000
SCI_MARKERDEFINE=2040
SCI_MARKERENABLEHIGHLIGHT=2293
SCI_MARKERADD=2043
SCI_MARKERDELETE=2044
SCI_MARKERDELETEALL=2045
SCI_MARKERGET=2046
SCI_MARKERNEXT=2047
SCI_MARKERPREVIOUS=2048
SCI_MARKERDEFINEPIXMAP=2049
SCI_MARKERADDSET=2466
SC_MAX_MARGIN=4
SC_MARGIN_SYMBOL=0
SC_MARGIN_NUMBER=1
SC_MARGIN_BACK=2
SC_MARGIN_FORE=3
SC_MARGIN_TEXT=4
SC_MARGIN_RTEXT=5
SC_MARGIN_COLOUR=6
STYLE_DEFAULT=32
STYLE_LINENUMBER=33
STYLE_BRACELIGHT=34
STYLE_BRACEBAD=35
STYLE_CONTROLCHAR=36
STYLE_INDENTGUIDE=37
STYLE_CALLTIP=38
STYLE_FOLDDISPLAYTEXT=39
STYLE_LASTPREDEFINED=39
STYLE_MAX=255
SC_CHARSET_ANSI=0
SC_CHARSET_DEFAULT=1
SC_CHARSET_BALTIC=186
SC_CHARSET_CHINESEBIG5=136
SC_CHARSET_EASTEUROPE=238
SC_CHARSET_GB2312=134
SC_CHARSET_GREEK=161
SC_CHARSET_HANGUL=129
SC_CHARSET_MAC=77
SC_CHARSET_OEM=255
SC_CHARSET_RUSSIAN=204
SC_CHARSET_OEM866=866
SC_CHARSET_CYRILLIC=1251
SC_CHARSET_SHIFTJIS=128
SC_CHARSET_SYMBOL=2
SC_CHARSET_TURKISH=162
SC_CHARSET_JOHAB=130
SC_CHARSET_HEBREW=177
SC_CHARSET_ARABIC=178
SC_CHARSET_VIETNAMESE=163
SC_CHARSET_THAI=222
SC_CHARSET_8859_15=1000
SCI_STYLECLEARALL=2050
SCI_STYLERESETDEFAULT=2058
SC_CASE_MIXED=0
SC_CASE_UPPER=1
SC_CASE_LOWER=2
SC_CASE_CAMEL=3
SC_FONT_SIZE_MULTIPLIER=100
SC_WEIGHT_NORMAL=400
SC_WEIGHT_SEMIBOLD=600
SC_WEIGHT_BOLD=700
SC_ELEMENT_LIST=0
SC_ELEMENT_LIST_BACK=1
SC_ELEMENT_LIST_SELECTED=2
SC_ELEMENT_LIST_SELECTED_BACK=3
SC_ELEMENT_SELECTION_TEXT=10
SC_ELEMENT_SELECTION_BACK=11
SC_ELEMENT_SELECTION_ADDITIONAL_TEXT=12
SC_ELEMENT_SELECTION_ADDITIONAL_BACK=13
SC_ELEMENT_SELECTION_SECONDARY_TEXT=14
SC_ELEMENT_SELECTION_SECONDARY_BACK=15
SC_ELEMENT_SELECTION_INACTIVE_TEXT=16
SC_ELEMENT_SELECTION_INACTIVE_BACK=17
SC_ELEMENT_CARET=40
SC_ELEMENT_CARET_ADDITIONAL=41
SC_ELEMENT_CARET_LINE_BACK=50
SC_ELEMENT_WHITE_SPACE=60
SC_ELEMENT_WHITE_SPACE_BACK=61
SC_ELEMENT_HOT_SPOT_ACTIVE=70
SC_ELEMENT_HOT_SPOT_ACTIVE_BACK=71
SCI_RESETELEMENTCOLOUR=2755
SCI_SETSELFORE=2067
SCI_SETSELBACK=2068
SC_LAYER_BASE=0
SC_LAYER_UNDER_TEXT=1
SC_LAYER_OVER_TEXT=2
SCI_ASSIGNCMDKEY=2070
SCI_CLEARCMDKEY=2071
SCI_CLEARALLCMDKEYS=2072
SCI_SETSTYLINGEX=2073
SCI_BEGINUNDOACTION=2078
SCI_ENDUNDOACTION=2079
INDIC_PLAIN=0
INDIC_SQUIGGLE=1
INDIC_TT=2
INDIC_DIAGONAL=3
INDIC_STRIKE=4
INDIC_HIDDEN=5
INDIC_BOX=6
INDIC_ROUNDBOX=7
INDIC_STRAIGHTBOX=8
INDIC_DASH=9
INDIC_DOTS=10
INDIC_SQUIGGLELOW=11
INDIC_DOTBOX=12
INDIC_SQUIGGLEPIXMAP=13
INDIC_COMPOSITIONTHICK=14
INDIC_COMPOSITIONTHIN=15
INDIC_FULLBOX=16
INDIC_TEXTFORE=17
INDIC_POINT=18
INDIC_POINTCHARACTER=19
INDIC_GRADIENT=20
INDIC_GRADIENTCENTRE=21
INDIC_CONTAINER=8
INDIC_IME=32
INDIC_IME_MAX=35
INDIC_MAX=35
INDICATOR_CONTAINER=8
INDICATOR_IME=32
INDICATOR_IME_MAX=35
INDICATOR_MAX=35
SC_INDICVALUEBIT=0x1000000
SC_INDICVALUEMASK=0xFFFFFF
SC_INDICFLAG_NONE=0
SC_INDICFLAG_VALUEFORE=1
SCI_SETWHITESPACEFORE=2084
SCI_SETWHITESPACEBACK=2085
SCI_AUTOCSHOW=2100
SCI_AUTOCCANCEL=2101
SCI_AUTOCACTIVE=2102
SCI_AUTOCPOSSTART=2103
SCI_AUTOCCOMPLETE=2104
SCI_AUTOCSTOPS=2105
SCI_AUTOCSELECT=2108
SCI_USERLISTSHOW=2117
SCI_REGISTERIMAGE=2405
SCI_CLEARREGISTEREDIMAGES=2408
SCI_COUNTCHARACTERS=2633
SCI_COUNTCODEUNITS=2715
SC_IV_NONE=0
SC_IV_REAL=1
SC_IV_LOOKFORWARD=2
SC_IV_LOOKBOTH=3
SCI_SETEMPTYSELECTION=2556
SC_PRINT_NORMAL=0
SC_PRINT_INVERTLIGHT=1
SC_PRINT_BLACKONWHITE=2
SC_PRINT_COLOURONWHITE=3
SC_PRINT_COLOURONWHITEDEFAULTBG=4
SC_PRINT_SCREENCOLOURS=5
SCFIND_NONE=0x0
SCFIND_WHOLEWORD=0x2
SCFIND_MATCHCASE=0x4
SCFIND_WORDSTART=0x00100000
SCFIND_REGEXP=0x00200000
SCFIND_POSIX=0x00400000
SCFIND_CXX11REGEX=0x00800000
SCI_FINDTEXT=2150
SCI_FORMATRANGE=2151
SCI_GETLINE=2153
SCI_SETSEL=2160
SCI_GETSELTEXT=2161
SCI_GETTEXTRANGE=2162
SCI_HIDESELECTION=2163
SCI_POINTXFROMPOSITION=2164
SCI_POINTYFROMPOSITION=2165
SCI_LINEFROMPOSITION=2166
SCI_POSITIONFROMLINE=2167
SCI_LINESCROLL=2168
SCI_SCROLLCARET=2169
SCI_SCROLLRANGE=2569
SCI_REPLACESEL=2170
SCI_NULL=2172
SCI_CANPASTE=2173
SCI_CANUNDO=2174
SCI_EMPTYUNDOBUFFER=2175
SCI_UNDO=2176
SCI_CUT=2177
SCI_COPY=2178
SCI_PASTE=2179
SCI_CLEAR=2180
SCI_SETTEXT=2181
SCI_GETTEXT=2182
SCI_SETTARGETRANGE=2686
SCI_TARGETFROMSELECTION=2287
SCI_TARGETWHOLEDOCUMENT=2690
SCI_REPLACETARGET=2194
SCI_REPLACETARGETRE=2195
SCI_SEARCHINTARGET=2197
SCI_CALLTIPSHOW=2200
SCI_CALLTIPCANCEL=2201
SCI_CALLTIPACTIVE=2202
SCI_CALLTIPPOSSTART=2203
SCI_CALLTIPSETHLT=2204
SCI_VISIBLEFROMDOCLINE=2220
SCI_DOCLINEFROMVISIBLE=2221
SCI_WRAPCOUNT=2235
SC_FOLDLEVELNONE=0x0
SC_FOLDLEVELBASE=0x400
SC_FOLDLEVELWHITEFLAG=0x1000
SC_FOLDLEVELHEADERFLAG=0x2000
SC_FOLDLEVELNUMBERMASK=0x0FFF
SCI_SHOWLINES=2226
SCI_HIDELINES=2227
SCI_TOGGLEFOLD=2231
SCI_TOGGLEFOLDSHOWTEXT=2700
SC_FOLDDISPLAYTEXT_HIDDEN=0
SC_FOLDDISPLAYTEXT_STANDARD=1
SC_FOLDDISPLAYTEXT_BOXED=2
SCI_SETDEFAULTFOLDDISPLAYTEXT=2722
SCI_GETDEFAULTFOLDDISPLAYTEXT=2723
SC_FOLDACTION_CONTRACT=0
SC_FOLDACTION_EXPAND=1
SC_FOLDACTION_TOGGLE=2
SCI_FOLDLINE=2237
SCI_FOLDCHILDREN=2238
SCI_EXPANDCHILDREN=2239
SCI_FOLDALL=2662
SCI_ENSUREVISIBLE=2232
SC_AUTOMATICFOLD_NONE=0x0000
SC_AUTOMATICFOLD_SHOW=0x0001
SC_AUTOMATICFOLD_CLICK=0x0002
SC_AUTOMATICFOLD_CHANGE=0x0004
SC_FOLDFLAG_NONE=0x0000
SC_FOLDFLAG_LINEBEFORE_EXPANDED=0x0002
SC_FOLDFLAG_LINEBEFORE_CONTRACTED=0x0004
SC_FOLDFLAG_LINEAFTER_EXPANDED=0x0008
SC_FOLDFLAG_LINEAFTER_CONTRACTED=0x0010
SC_FOLDFLAG_LEVELNUMBERS=0x0040
SC_FOLDFLAG_LINESTATE=0x0080
SCI_ENSUREVISIBLEENFORCEPOLICY=2234
SC_TIME_FOREVER=10000000
SCI_WORDSTARTPOSITION=2266
SCI_WORDENDPOSITION=2267
SCI_ISRANGEWORD=2691
SC_IDLESTYLING_NONE=0
SC_IDLESTYLING_TOVISIBLE=1
SC_IDLESTYLING_AFTERVISIBLE=2
SC_IDLESTYLING_ALL=3
SC_WRAP_NONE=0
SC_WRAP_WORD=1
SC_WRAP_CHAR=2
SC_WRAP_WHITESPACE=3
SC_WRAPVISUALFLAG_NONE=0x0000
SC_WRAPVISUALFLAG_END=0x0001
SC_WRAPVISUALFLAG_START=0x0002
SC_WRAPVISUALFLAG_MARGIN=0x0004
SC_WRAPVISUALFLAGLOC_DEFAULT=0x0000
SC_WRAPVISUALFLAGLOC_END_BY_TEXT=0x0001
SC_WRAPVISUALFLAGLOC_START_BY_TEXT=0x0002
SC_WRAPINDENT_FIXED=0
SC_WRAPINDENT_SAME=1
SC_WRAPINDENT_INDENT=2
SC_WRAPINDENT_DEEPINDENT=3
SC_CACHE_NONE=0
SC_CACHE_CARET=1
SC_CACHE_PAGE=2
SC_CACHE_DOCUMENT=3
SCI_TEXTWIDTH=2276
SCI_TEXTHEIGHT=2279
SCI_APPENDTEXT=2282
SC_PHASES_ONE=0
SC_PHASES_TWO=1
SC_PHASES_MULTIPLE=2
SC_EFF_QUALITY_MASK=0xF
SC_EFF_QUALITY_DEFAULT=0
SC_EFF_QUALITY_NON_ANTIALIASED=1
SC_EFF_QUALITY_ANTIALIASED=2
SC_EFF_QUALITY_LCD_OPTIMIZED=3
SC_MULTIPASTE_ONCE=0
SC_MULTIPASTE_EACH=1
SCI_LINESJOIN=2288
SCI_LINESSPLIT=2289
SCI_SETFOLDMARGINCOLOUR=2290
SCI_SETFOLDMARGINHICOLOUR=2291
SC_ACCESSIBILITY_DISABLED=0
SC_ACCESSIBILITY_ENABLED=1
SCI_LINEDOWN=2300
SCI_LINEDOWNEXTEND=2301
SCI_LINEUP=2302
SCI_LINEUPEXTEND=2303
SCI_CHARLEFT=2304
SCI_CHARLEFTEXTEND=2305
SCI_CHARRIGHT=2306
SCI_CHARRIGHTEXTEND=2307
SCI_WORDLEFT=2308
SCI_WORDLEFTEXTEND=2309
SCI_WORDRIGHT=2310
SCI_WORDRIGHTEXTEND=2311
SCI_HOME=2312
SCI_HOMEEXTEND=2313
SCI_LINEEND=2314
SCI_LINEENDEXTEND=2315
SCI_DOCUMENTSTART=2316
SCI_DOCUMENTSTARTEXTEND=2317
SCI_DOCUMENTEND=2318
SCI_DOCUMENTENDEXTEND=2319
SCI_PAGEUP=2320
SCI_PAGEUPEXTEND=2321
SCI_PAGEDOWN=2322
SCI_PAGEDOWNEXTEND=2323
SCI_EDITTOGGLEOVERTYPE=2324
SCI_CANCEL=2325
SCI_DELETEBACK=2326
SCI_TAB=2327
SCI_BACKTAB=2328
SCI_NEWLINE=2329
SCI_FORMFEED=2330
SCI_VCHOME=2331
SCI_VCHOMEEXTEND=2332
SCI_ZOOMIN=2333
SCI_ZOOMOUT=2334
SCI_DELWORDLEFT=2335
SCI_DELWORDRIGHT=2336
SCI_DELWORDRIGHTEND=2518
SCI_LINECUT=2337
SCI_LINEDELETE=2338
SCI_LINETRANSPOSE=2339
SCI_LINEREVERSE=2354
SCI_LINEDUPLICATE=2404
SCI_LOWERCASE=2340
SCI_UPPERCASE=2341
SCI_LINESCROLLDOWN=2342
SCI_LINESCROLLUP=2343
SCI_DELETEBACKNOTLINE=2344
SCI_HOMEDISPLAY=2345
SCI_HOMEDISPLAYEXTEND=2346
SCI_LINEENDDISPLAY=2347
SCI_LINEENDDISPLAYEXTEND=2348
SCI_HOMEWRAP=2349
SCI_HOMEWRAPEXTEND=2450
SCI_LINEENDWRAP=2451
SCI_LINEENDWRAPEXTEND=2452
SCI_VCHOMEWRAP=2453
SCI_VCHOMEWRAPEXTEND=2454
SCI_LINECOPY=2455
SCI_MOVECARETINSIDEVIEW=2401
SCI_LINELENGTH=2350
SCI_BRACEHIGHLIGHT=2351
SCI_BRACEHIGHLIGHTINDICATOR=2498
SCI_BRACEBADLIGHT=2352
SCI_BRACEBADLIGHTINDICATOR=2499
SCI_BRACEMATCH=2353
SCI_BRACEMATCHNEXT=2369
EDGE_NONE=0
EDGE_LINE=1
EDGE_BACKGROUND=2
EDGE_MULTILINE=3
SCI_MULTIEDGEADDLINE=2694
SCI_MULTIEDGECLEARALL=2695
SCI_SEARCHANCHOR=2366
SCI_SEARCHNEXT=2367
SCI_SEARCHPREV=2368
SC_POPUP_NEVER=0
SC_POPUP_ALL=1
SC_POPUP_TEXT=2
SCI_USEPOPUP=2371
SC_DOCUMENTOPTION_DEFAULT=0
SC_DOCUMENTOPTION_STYLES_NONE=0x1
SC_DOCUMENTOPTION_TEXT_LARGE=0x100
SCI_CREATEDOCUMENT=2375
SCI_ADDREFDOCUMENT=2376
SCI_RELEASEDOCUMENT=2377
SC_STATUS_OK=0
SC_STATUS_FAILURE=1
SC_STATUS_BADALLOC=2
SC_STATUS_WARN_START=1000
SC_STATUS_WARN_REGEX=1001
SCI_WORDPARTLEFT=2390
SCI_WORDPARTLEFTEXTEND=2391
SCI_WORDPARTRIGHT=2392
SCI_WORDPARTRIGHTEXTEND=2393
VISIBLE_SLOP=0x01
VISIBLE_STRICT=0x04
SCI_SETVISIBLEPOLICY=2394
SCI_DELLINELEFT=2395
SCI_DELLINERIGHT=2396
SCI_CHOOSECARETX=2399
SCI_GRABFOCUS=2400
CARET_SLOP=0x01
CARET_STRICT=0x04
CARET_JUMPS=0x10
CARET_EVEN=0x08
SCI_SETXCARETPOLICY=2402
SCI_SETYCARETPOLICY=2403
SCI_PARADOWN=2413
SCI_PARADOWNEXTEND=2414
SCI_PARAUP=2415
SCI_PARAUPEXTEND=2416
SCI_POSITIONBEFORE=2417
SCI_POSITIONAFTER=2418
SCI_POSITIONRELATIVE=2670
SCI_POSITIONRELATIVECODEUNITS=2716
SCI_COPYRANGE=2419
SCI_COPYTEXT=2420
SC_SEL_STREAM=0
SC_SEL_RECTANGLE=1
SC_SEL_LINES=2
SC_SEL_THIN=3
SCI_GETLINESELSTARTPOSITION=2424
SCI_GETLINESELENDPOSITION=2425
SCI_LINEDOWNRECTEXTEND=2426
SCI_LINEUPRECTEXTEND=2427
SCI_CHARLEFTRECTEXTEND=2428
SCI_CHARRIGHTRECTEXTEND=2429
SCI_HOMERECTEXTEND=2430
SCI_VCHOMERECTEXTEND=2431
SCI_LINEENDRECTEXTEND=2432
SCI_PAGEUPRECTEXTEND=2433
SCI_PAGEDOWNRECTEXTEND=2434
SCI_STUTTEREDPAGEUP=2435
SCI_STUTTEREDPAGEUPEXTEND=2436
SCI_STUTTEREDPAGEDOWN=2437
SCI_STUTTEREDPAGEDOWNEXTEND=2438
SCI_WORDLEFTEND=2439
SCI_WORDLEFTENDEXTEND=2440
SCI_WORDRIGHTEND=2441
SCI_WORDRIGHTENDEXTEND=2442
SCI_SETCHARSDEFAULT=2444
SC_CASEINSENSITIVEBEHAVIOUR_RESPECTCASE=0
SC_CASEINSENSITIVEBEHAVIOUR_IGNORECASE=1
SC_MULTIAUTOC_ONCE=0
SC_MULTIAUTOC_EACH=1
SC_ORDER_PRESORTED=0
SC_ORDER_PERFORMSORT=1
SC_ORDER_CUSTOM=2
SCI_ALLOCATE=2446
SCI_TARGETASUTF8=2447
SCI_SETLENGTHFORENCODE=2448
SCI_ENCODEDFROMUTF8=2449
SCI_FINDCOLUMN=2456
SC_CARETSTICKY_OFF=0
SC_CARETSTICKY_ON=1
SC_CARETSTICKY_WHITESPACE=2
SCI_TOGGLECARETSTICKY=2459
SCI_REPLACERECTANGULAR=2771
SCI_SELECTIONDUPLICATE=2469
CARETSTYLE_INVISIBLE=0
CARETSTYLE_LINE=1
CARETSTYLE_BLOCK=2
CARETSTYLE_OVERSTRIKE_BAR=0
CARETSTYLE_OVERSTRIKE_BLOCK=0x10
CARETSTYLE_INS_MASK=0xF
CARETSTYLE_BLOCK_AFTER=0x100
SCI_INDICATORFILLRANGE=2504
SCI_INDICATORCLEARRANGE=2505
SCI_INDICATORALLONFOR=2506
SCI_INDICATORVALUEAT=2507
SCI_INDICATORSTART=2508
SCI_INDICATOREND=2509
SCI_COPYALLOWLINE=2519
SCI_MARKERSYMBOLDEFINED=2529
SCI_MARGINTEXTCLEARALL=2536
SC_MARGINOPTION_NONE=0
SC_MARGINOPTION_SUBLINESELECT=1
SCI_ANNOTATIONCLEARALL=2547
ANNOTATION_HIDDEN=0
ANNOTATION_STANDARD=1
ANNOTATION_BOXED=2
ANNOTATION_INDENTED=3
SCI_RELEASEALLEXTENDEDSTYLES=2552
SCI_ALLOCATEEXTENDEDSTYLES=2553
UNDO_NONE=0
UNDO_MAY_COALESCE=1
SCI_ADDUNDOACTION=2560
SCI_CHARPOSITIONFROMPOINT=2561
SCI_CHARPOSITIONFROMPOINTCLOSE=2562
SCI_CLEARSELECTIONS=2571
SCI_SETSELECTION=2572
SCI_ADDSELECTION=2573
SCI_DROPSELECTIONN=2671
SCVS_NONE=0
SCVS_RECTANGULARSELECTION=1
SCVS_USERACCESSIBLE=2
SCVS_NOWRAPLINESTART=4
SCI_ROTATESELECTION=2606
SCI_SWAPMAINANCHORCARET=2607
SCI_MULTIPLESELECTADDNEXT=2688
SCI_MULTIPLESELECTADDEACH=2689
SCI_CHANGELEXERSTATE=2617
SCI_CONTRACTEDFOLDNEXT=2618
SCI_VERTICALCENTRECARET=2619
SCI_MOVESELECTEDLINESUP=2620
SCI_MOVESELECTEDLINESDOWN=2621
SCI_MARKERDEFINERGBAIMAGE=2626
SCI_REGISTERRGBAIMAGE=2627
SCI_SCROLLTOSTART=2628
SCI_SCROLLTOEND=2629
SC_TECHNOLOGY_DEFAULT=0
SC_TECHNOLOGY_DIRECTWRITE=1
SC_TECHNOLOGY_DIRECTWRITERETAIN=2
SC_TECHNOLOGY_DIRECTWRITEDC=3
SCI_CREATELOADER=2632
SCI_FINDINDICATORSHOW=2640
SCI_FINDINDICATORFLASH=2641
SCI_FINDINDICATORHIDE=2642
SCI_VCHOMEDISPLAY=2652
SCI_VCHOMEDISPLAYEXTEND=2653
SC_LINE_END_TYPE_DEFAULT=0
SC_LINE_END_TYPE_UNICODE=1
SCI_CLEARREPRESENTATION=2667
SCI_CLEARALLREPRESENTATIONS=2770
SC_REPRESENTATION_PLAIN=0
SC_REPRESENTATION_BLOB=1
SC_REPRESENTATION_COLOUR=0x10
SCI_EOLANNOTATIONCLEARALL=2744
EOLANNOTATION_HIDDEN=0x0
EOLANNOTATION_STANDARD=0x1
EOLANNOTATION_BOXED=0x2
EOLANNOTATION_STADIUM=0x100
EOLANNOTATION_FLAT_CIRCLE=0x101
EOLANNOTATION_ANGLE_CIRCLE=0x102
EOLANNOTATION_CIRCLE_FLAT=0x110
EOLANNOTATION_FLATS=0x111
EOLANNOTATION_ANGLE_FLAT=0x112
EOLANNOTATION_CIRCLE_ANGLE=0x120
EOLANNOTATION_FLAT_ANGLE=0x121
EOLANNOTATION_ANGLES=0x122
SC_SUPPORTS_LINE_DRAWS_FINAL=0
SC_SUPPORTS_PIXEL_DIVISIONS=1
SC_SUPPORTS_FRACTIONAL_STROKE_WIDTH=2
SC_SUPPORTS_TRANSLUCENT_STROKE=3
SC_SUPPORTS_PIXEL_MODIFICATION=4
SC_LINECHARACTERINDEX_NONE=0
SC_LINECHARACTERINDEX_UTF32=1
SC_LINECHARACTERINDEX_UTF16=2
SCI_ALLOCATELINECHARACTERINDEX=2711
SCI_RELEASELINECHARACTERINDEX=2712
SCI_LINEFROMINDEXPOSITION=2713
SCI_INDEXPOSITIONFROMLINE=2714
SCI_STARTRECORD=3001
SCI_STOPRECORD=3002
SCI_COLOURISE=4003
KEYWORDSET_MAX=8
SCI_PRIVATELEXERCALL=4013
SCI_PROPERTYNAMES=4014
SC_TYPE_BOOLEAN=0
SC_TYPE_INTEGER=1
SC_TYPE_STRING=2
SCI_PROPERTYTYPE=4015
SCI_DESCRIBEPROPERTY=4016
SCI_DESCRIBEKEYWORDSETS=4017
SCI_ALLOCATESUBSTYLES=4020
SCI_FREESUBSTYLES=4023
SCI_NAMEOFSTYLE=4030
SCI_TAGSOFSTYLE=4031
SCI_DESCRIPTIONOFSTYLE=4032
SC_MOD_NONE=0x0
SC_MOD_INSERTTEXT=0x1
SC_MOD_DELETETEXT=0x2
SC_MOD_CHANGESTYLE=0x4
SC_MOD_CHANGEFOLD=0x8
SC_PERFORMED_USER=0x10
SC_PERFORMED_UNDO=0x20
SC_PERFORMED_REDO=0x40
SC_MULTISTEPUNDOREDO=0x80
SC_LASTSTEPINUNDOREDO=0x100
SC_MOD_CHANGEMARKER=0x200
SC_MOD_BEFOREINSERT=0x400
SC_MOD_BEFOREDELETE=0x800
SC_MULTILINEUNDOREDO=0x1000
SC_STARTACTION=0x2000
SC_MOD_CHANGEINDICATOR=0x4000
SC_MOD_CHANGELINESTATE=0x8000
SC_MOD_CHANGEMARGIN=0x10000
SC_MOD_CHANGEANNOTATION=0x20000
SC_MOD_CONTAINER=0x40000
SC_MOD_LEXERSTATE=0x80000
SC_MOD_INSERTCHECK=0x100000
SC_MOD_CHANGETABSTOPS=0x200000
SC_MOD_CHANGEEOLANNOTATION=0x400000
SC_MODEVENTMASKALL=0x7FFFFF
SC_UPDATE_NONE=0x0
SC_UPDATE_CONTENT=0x1
SC_UPDATE_SELECTION=0x2
SC_UPDATE_V_SCROLL=0x4
SC_UPDATE_H_SCROLL=0x8
SCEN_CHANGE=768
SCEN_SETFOCUS=512
SCEN_KILLFOCUS=256
SCK_DOWN=300
SCK_UP=301
SCK_LEFT=302
SCK_RIGHT=303
SCK_HOME=304
SCK_END=305
SCK_PRIOR=306
SCK_NEXT=307
SCK_DELETE=308
SCK_INSERT=309
SCK_ESCAPE=7
SCK_BACK=8
SCK_TAB=9
SCK_RETURN=13
SCK_ADD=310
SCK_SUBTRACT=311
SCK_DIVIDE=312
SCK_WIN=313
SCK_RWIN=314
SCK_MENU=315
SCMOD_NORM=0
SCMOD_SHIFT=1
SCMOD_CTRL=2
SCMOD_ALT=4
SCMOD_SUPER=8
SCMOD_META=16
SC_AC_FILLUP=1
SC_AC_DOUBLECLICK=2
SC_AC_TAB=3
SC_AC_NEWLINE=4
SC_AC_COMMAND=5
SC_CHARACTERSOURCE_DIRECT_INPUT=0
SC_CHARACTERSOURCE_TENTATIVE_INPUT=1
SC_CHARACTERSOURCE_IME_RESULT=2
SCN_STYLENEEDED=2000
SCN_CHARADDED=2001
SCN_SAVEPOINTREACHED=2002
SCN_SAVEPOINTLEFT=2003
SCN_MODIFYATTEMPTRO=2004
SCN_KEY=2005
SCN_DOUBLECLICK=2006
SCN_UPDATEUI=2007
SCN_MODIFIED=2008
SCN_MACRORECORD=2009
SCN_MARGINCLICK=2010
SCN_NEEDSHOWN=2011
SCN_PAINTED=2013
SCN_USERLISTSELECTION=2014
SCN_URIDROPPED=2015
SCN_DWELLSTART=2016
SCN_DWELLEND=2017
SCN_ZOOM=2018
SCN_HOTSPOTCLICK=2019
SCN_HOTSPOTDOUBLECLICK=2020
SCN_CALLTIPCLICK=2021
SCN_AUTOCSELECTION=2022
SCN_INDICATORCLICK=2023
SCN_INDICATORRELEASE=2024
SCN_AUTOCCANCELLED=2025
SCN_AUTOCCHARDELETED=2026
SCN_HOTSPOTRELEASECLICK=2027
SCN_FOCUSIN=2028
SCN_FOCUSOUT=2029
SCN_AUTOCCOMPLETED=2030
SCN_MARGINRIGHTCLICK=2031
SCN_AUTOCSELECTIONCHANGE=2032
SC_BIDIRECTIONAL_DISABLED=0
SC_BIDIRECTIONAL_L2R=1
SC_BIDIRECTIONAL_R2L=2
# --Autogenerated -- end of section automatically generated from Scintilla.iface */
