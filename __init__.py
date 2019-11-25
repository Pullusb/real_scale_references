# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "Real scale references",
    "author" : "Samuel Bernou",
    "description" : "Link some references models at real world scale",
    "blender" : (2, 80, 0),
    "version" : (1, 1, 0),
    "location" : "3D view > sidebar 'N' > View > Real scale ref",
    "wiki_url": "https://github.com/Pullusb/real_scale_references",
    "warning" : "",
    "category" : "3D View"
}

import bpy
import os
from os.path import dirname, join, exists
from mathutils import Vector

import bpy
from sys import platform
import subprocess
import os

def openFolder(folderpath):
    """
    open the folder at the path given
    with cmd relative to user's OS
    """
    myOS = platform
    if myOS.startswith('linux') or myOS.startswith('freebsd'):
        # linux
        cmd = 'xdg-open'
        #print("operating system : Linux")
    elif myOS.startswith('win'):
        # Windows
        #cmd = 'start '
        cmd = 'explorer'
        #print("operating system : Windows")
        if not folderpath:
            return('/')

    else:#elif myOS == "darwin":
        # OS X
        #print("operating system : MACos")
        cmd = 'open'

    if not folderpath:
        return('//')

    # to prevent bad path string use normpath:
    folderpath = os.path.normpath(folderpath)

    fullcmd = [cmd, folderpath]
    print(fullcmd)
    subprocess.Popen(fullcmd)
    return ' '.join(fullcmd)#back to string to return and print

def add_gyzmo_manipulator():
    name = "references_gyzmo"
    verts = [Vector((-8.811301910327529e-08, 0.2563393712043762, 0.0)), Vector((-0.050009336322546005, 0.25141388177871704, 0.0)), Vector((-0.0980968251824379, 0.23682671785354614, 0.0)), Vector((-0.14241451025009155, 0.2131384164094925, 0.0)), Vector((-0.18125927448272705, 0.18125934898853302, 0.0)), Vector((-0.2131383717060089, 0.14241455495357513, 0.0)), Vector((-0.23682665824890137, 0.09809687733650208, 0.0)), Vector((-0.25141382217407227, 0.05000941455364227, 0.0)), Vector((-0.25633934140205383, 1.0926061122518149e-07, 0.0)), Vector((-0.25141382217407227, -0.050009194761514664, 0.0)), Vector((-0.23682665824890137, -0.09809668362140656, 0.0)), Vector((-0.2131383717060089, -0.1424143761396408, 0.0)), Vector((-0.18125928938388824, -0.1812591701745987, 0.0)), Vector((-0.14241449534893036, -0.21313825249671936, 0.0)), Vector((-0.09809678792953491, -0.2368265688419342, 0.0)), Vector((-0.05000927671790123, -0.2514137327671051, 0.0)), Vector((5.89343436274703e-08, -0.2563391923904419, 0.0)), Vector((0.05000939220190048, -0.2514137029647827, 0.0)), Vector((0.09809688478708267, -0.23682649433612823, 0.0)), Vector((0.14241456985473633, -0.2131381630897522, 0.0)), Vector((0.18125933408737183, -0.18125906586647034, 0.0)), Vector((0.2131384015083313, -0.14241424202919006, 0.0)), Vector((0.23682667315006256, -0.09809652715921402, 0.0)), Vector((0.25141382217407227, -0.050009001046419144, 0.0)), Vector((0.25633925199508667, 3.360787843575963e-07, 0.0)), Vector((0.2514137029647827, 0.05000967159867287, 0.0)), Vector((0.23682647943496704, 0.09809715300798416, 0.0)), Vector((0.213138148188591, 0.14241482317447662, 0.0)), Vector((0.18125897645950317, 0.18125954270362854, 0.0)), Vector((0.1424141675233841, 0.21313859522342682, 0.0)), Vector((0.09809643030166626, 0.2368268370628357, 0.0)), Vector((0.050008974969387054, 0.2514139413833618, 0.0)), Vector((-9.417013302481791e-08, 0.2862257957458496, 0.0)), Vector((-0.05583987385034561, 0.28072595596313477, 0.0)), Vector((-0.10953382402658463, 0.26443809270858765, 0.0)), Vector((-0.15901847183704376, 0.23798801004886627, 0.0)), Vector((-0.2023921012878418, 0.20239216089248657, 0.0)), Vector((-0.2379879355430603, 0.15901848673820496, 0.0)), Vector((-0.26443803310394287, 0.1095338836312294, 0.0)), Vector((-0.28072589635849, 0.05583995208144188, 0.0)), Vector((-0.28622567653656006, 9.867795824902714e-08, 0.0)), Vector((-0.2807259261608124, -0.05583973973989487, 0.0)), Vector((-0.26443806290626526, -0.10953370481729507, 0.0)), Vector((-0.2379879355430603, -0.1590183675289154, 0.0)), Vector((-0.2023921012878418, -0.20239202678203583, 0.0)), Vector((-0.15901847183704376, -0.23798786103725433, 0.0)), Vector((-0.10953379422426224, -0.2644379138946533, 0.0)), Vector((-0.05583981052041054, -0.2807258069515228, 0.0)), Vector((7.163795601172751e-08, -0.28622549772262573, 0.0)), Vector((0.05583994835615158, -0.28072577714920044, 0.0)), Vector((0.10953392833471298, -0.26443782448768616, 0.0)), Vector((0.15901857614517212, -0.23798774182796478, 0.0)), Vector((0.20239220559597015, -0.2023918777704239, 0.0)), Vector((0.23798802495002747, -0.15901820361614227, 0.0)), Vector((0.26443809270858765, -0.10953351855278015, 0.0)), Vector((0.2807259261608124, -0.055839527398347855, 0.0)), Vector((0.28622564673423767, 3.5360793049221684e-07, 0.0)), Vector((0.2807258367538452, 0.05584022402763367, 0.0)), Vector((0.26443785429000854, 0.10953418165445328, 0.0)), Vector((0.2379877120256424, 0.15901879966259003, 0.0)), Vector((0.20239178836345673, 0.20239239931106567, 0.0)), Vector((0.15901809930801392, 0.23798824846744537, 0.0)), Vector((0.1095334142446518, 0.264438271522522, 0.0)), Vector((0.05583947151899338, 0.2807261049747467, 0.0)), Vector((-0.025125578045845032, 0.2551040053367615, 0.0)), Vector((-0.07441110163927078, 0.2453005015850067, 0.0)), Vector((-0.12083707004785538, 0.22607025504112244, 0.0)), Vector((-0.16261932253837585, 0.19815224409103394, 0.0)), Vector((-0.19815221428871155, 0.16261936724185944, 0.0)), Vector((-0.22607022523880005, 0.12083711475133896, 0.0)), Vector((-0.24530047178268433, 0.07441116869449615, 0.0)), Vector((-0.2551039755344391, 0.025125645101070404, 0.0)), Vector((-0.2551039755344391, -0.02512543462216854, 0.0)), Vector((-0.24530048668384552, -0.07441095262765884, 0.0)), Vector((-0.22607022523880005, -0.12083692103624344, 0.0)), Vector((-0.19815219938755035, -0.1626191884279251, 0.0)), Vector((-0.16261930763721466, -0.1981521099805832, 0.0)), Vector((-0.12083703279495239, -0.2260701209306717, 0.0)), Vector((-0.0744110494852066, -0.24530038237571716, 0.0)), Vector((-0.025125496089458466, -0.2551038861274719, 0.0)), Vector((0.025125613436102867, -0.25510385632514954, 0.0)), Vector((0.07441115379333496, -0.2453003078699112, 0.0)), Vector((0.12083712220191956, -0.22607003152370453, 0.0)), Vector((0.16261938214302063, -0.19815199077129364, 0.0)), Vector((0.19815224409103394, -0.16261908411979675, 0.0)), Vector((0.22607025504112244, -0.1208367794752121, 0.0)), Vector((0.24530048668384552, -0.07441077381372452, 0.0)), Vector((0.2551039159297943, -0.025125224143266678, 0.0)), Vector((0.2551038861274719, 0.025125889107584953, 0.0)), Vector((0.2453003227710724, 0.07441142946481705, 0.0)), Vector((0.22606998682022095, 0.12083738297224045, 0.0)), Vector((0.19815191626548767, 0.16261960566043854, 0.0)), Vector((0.1626189947128296, 0.19815245270729065, 0.0)), Vector((0.12083668261766434, 0.22607041895389557, 0.0)), Vector((0.07441069930791855, 0.24530063569545746, 0.0)), Vector((0.025125328451395035, 0.25510406494140625, 0.0)), Vector((-0.028054937720298767, 0.28484636545181274, 0.0)), Vector((-0.08308663219213486, 0.2738999128341675, 0.0)), Vector((-0.13492533564567566, 0.2524275779724121, 0.0)), Vector((-0.18157893419265747, 0.2212546318769455, 0.0)), Vector((-0.22125457227230072, 0.18157896399497986, 0.0)), Vector((-0.25242748856544495, 0.13492536544799805, 0.0)), Vector((-0.27389979362487793, 0.08308668434619904, 0.0)), Vector((-0.2848462462425232, 0.02805499918758869, 0.0)), Vector((-0.2848462760448456, -0.02805480919778347, 0.0)), Vector((-0.2738998532295227, -0.08308648318052292, 0.0)), Vector((-0.25242751836776733, -0.13492518663406372, 0.0)), Vector((-0.22125457227230072, -0.1815788298845291, 0.0)), Vector((-0.18157893419265747, -0.22125446796417236, 0.0)), Vector((-0.13492529094219208, -0.2524273991584778, 0.0)), Vector((-0.08308656513690948, -0.2738996744155884, 0.0)), Vector((-0.028054852038621902, -0.28484612703323364, 0.0)), Vector((0.028054995462298393, -0.28484612703323364, 0.0)), Vector((0.08308669179677963, -0.2738996148109436, 0.0)), Vector((0.13492542505264282, -0.2524273097515106, 0.0)), Vector((0.18157902359962463, -0.2212543487548828, 0.0)), Vector((0.2212546467781067, -0.18157869577407837, 0.0)), Vector((0.2524275779724121, -0.13492505252361298, 0.0)), Vector((0.2738998234272003, -0.0830862820148468, 0.0)), Vector((0.2848462760448456, -0.028054574504494667, 0.0)), Vector((0.2848462760448456, 0.02805526740849018, 0.0)), Vector((0.2738996744155884, 0.08308696746826172, 0.0)), Vector((0.2524273097515106, 0.13492564857006073, 0.0)), Vector((0.22125428915023804, 0.18157926201820374, 0.0)), Vector((0.1815786063671112, 0.2212548702955246, 0.0)), Vector((0.13492494821548462, 0.2524277865886688, 0.0)), Vector((0.08308617770671844, 0.27390003204345703, 0.0)), Vector((0.028054669499397278, 0.2848464548587799, 0.0)), Vector((-9.740835338334364e-08, 0.2960682511329651, 0.0)), Vector((-0.05776003748178482, 0.29037928581237793, 0.0)), Vector((-0.11330036073923111, 0.27353131771087646, 0.0)), Vector((-0.16448663175106049, 0.24617169797420502, 0.0)), Vector((-0.20935176312923431, 0.2093518078327179, 0.0)), Vector((-0.24617162346839905, 0.16448664665222168, 0.0)), Vector((-0.2735312581062317, 0.11330042034387589, 0.0)), Vector((-0.29037922620773315, 0.05776011943817139, 0.0)), Vector((-0.29606810212135315, 1.0207119771621365e-07, 0.0)), Vector((7.410137214947099e-08, -0.2960679233074188, 0.0)), Vector((0.05776011571288109, -0.2903790771961212, 0.0)), Vector((0.11330047249794006, -0.273531049489975, 0.0)), Vector((0.16448675096035004, -0.24617142975330353, 0.0)), Vector((0.20935186743736267, -0.2093515247106552, 0.0)), Vector((0.2461717128753662, -0.1644863784313202, 0.0)), Vector((0.27353131771087646, -0.11330004781484604, 0.0)), Vector((0.29037925601005554, -0.05775967985391617, 0.0)), Vector((0.29606807231903076, 3.6576741990757e-07, 0.0)), Vector((-0.029019663110375404, 0.2946413457393646, 0.0)), Vector((-0.08594372868537903, 0.28331848978996277, 0.0)), Vector((-0.13956500589847565, 0.26110780239105225, 0.0)), Vector((-0.18782289326190948, 0.22886289656162262, 0.0)), Vector((-0.22886283695697784, 0.18782292306423187, 0.0)), Vector((-0.2611077129840851, 0.13956503570079803, 0.0)), Vector((-0.2833184003829956, 0.0859437882900238, 0.0)), Vector((-0.29464125633239746, 0.029019726440310478, 0.0)), Vector((0.02901972271502018, -0.2946411371231079, 0.0)), Vector((0.0859437957406044, -0.2833181917667389, 0.0)), Vector((0.1395650953054428, -0.26110753417015076, 0.0)), Vector((0.18782299757003784, -0.22886262834072113, 0.0)), Vector((0.2288629114627838, -0.1878226399421692, 0.0)), Vector((0.26110780239105225, -0.13956472277641296, 0.0)), Vector((0.283318430185318, -0.08594337105751038, 0.0)), Vector((0.29464128613471985, -0.02901928685605526, 0.0)), Vector((-0.2418079674243927, 2.0064024397470348e-07, 0.0)), Vector((0.24180784821510315, 4.130550905756536e-07, 0.0)), Vector((-0.19249074161052704, 0.0396120548248291, 0.0)), Vector((-0.19249074161052704, -0.03961171582341194, 0.0)), Vector((0.19249065220355988, -0.039611563086509705, 0.0)), Vector((0.1924906224012375, 0.03961225599050522, 0.0)), Vector((-0.19249074161052704, 1.7500983062745945e-07, 0.0)), Vector((0.1924906224012375, 3.457262209849432e-07, 0.0)), Vector((-8.136417454807088e-05, 0.2085312306880951, 0.0)), Vector((-0.014971201308071613, 0.22765204310417175, 0.0)), Vector((-0.024572297930717468, 0.22765204310417175, 0.0)), Vector((-0.003986895550042391, 0.20153380930423737, 0.0)), Vector((-0.003986895550042391, 0.17216096818447113, 0.0)), Vector((0.003986895550042391, 0.17216096818447113, 0.0)), Vector((0.003986895550042391, 0.20145244896411896, 0.0)), Vector((0.024572297930717468, 0.22765204310417175, 0.0)), Vector((0.014971201308071613, 0.22765204310417175, 0.0))]
    edges = [(1, 64), (0, 64), (2, 65), (1, 65), (3, 66), (2, 66), (4, 67), (3, 67), (5, 68), (4, 68), (6, 69), (5, 69), (7, 70), (6, 70), (8, 71), (7, 71), (9, 72), (8, 72), (10, 73), (9, 73), (11, 74), (10, 74), (12, 75), (11, 75), (13, 76), (12, 76), (14, 77), (13, 77), (15, 78), (14, 78), (16, 79), (15, 79), (17, 80), (16, 80), (18, 81), (17, 81), (19, 82), (18, 82), (20, 83), (19, 83), (21, 84), (20, 84), (22, 85), (21, 85), (23, 86), (22, 86), (24, 87), (23, 87), (25, 88), (24, 88), (26, 89), (25, 89), (27, 90), (26, 90), (28, 91), (27, 91), (29, 92), (28, 92), (30, 93), (29, 93), (31, 94), (30, 94), (0, 95), (31, 95), (33, 96), (32, 96), (34, 97), (33, 97), (35, 98), (34, 98), (36, 99), (35, 99), (37, 100), (36, 100), (38, 101), (37, 101), (39, 102), (38, 102), (40, 103), (39, 103), (41, 104), (40, 104), (42, 105), (41, 105), (43, 106), (42, 106), (44, 107), (43, 107), (45, 108), (44, 108), (46, 109), (45, 109), (47, 110), (46, 110), (48, 111), (47, 111), (49, 112), (48, 112), (50, 113), (49, 113), (51, 114), (50, 114), (52, 115), (51, 115), (53, 116), (52, 116), (54, 117), (53, 117), (55, 118), (54, 118), (56, 119), (55, 119), (57, 120), (56, 120), (58, 121), (57, 121), (59, 122), (58, 122), (60, 123), (59, 123), (61, 124), (60, 124), (62, 125), (61, 125), (63, 126), (62, 126), (32, 127), (63, 127), (8, 40), (9, 41), (22, 54), (23, 55), (10, 42), (24, 56), (11, 43), (25, 57), (12, 44), (26, 58), (13, 45), (27, 59), (14, 46), (0, 32), (1, 33), (28, 60), (15, 47), (2, 34), (29, 61), (16, 48), (3, 35), (30, 62), (17, 49), (4, 36), (31, 63), (18, 50), (5, 37), (19, 51), (6, 38), (20, 52), (7, 39), (21, 53), (72, 104), (86, 118), (73, 105), (87, 119), (74, 106), (88, 120), (75, 107), (89, 121), (76, 108), (90, 122), (77, 109), (64, 96), (91, 123), (78, 110), (65, 97), (92, 124), (79, 111), (66, 98), (93, 125), (80, 112), (67, 99), (94, 126), (81, 113), (68, 100), (95, 127), (82, 114), (69, 101), (83, 115), (70, 102), (84, 116), (71, 103), (85, 117), (129, 146), (128, 146), (130, 147), (129, 147), (131, 148), (130, 148), (132, 149), (131, 149), (133, 150), (132, 150), (134, 151), (133, 151), (135, 152), (134, 152), (136, 153), (135, 153), (138, 154), (137, 154), (139, 155), (138, 155), (140, 156), (139, 156), (141, 157), (140, 157), (142, 158), (141, 158), (143, 159), (142, 159), (144, 160), (143, 160), (145, 161), (144, 161), (119, 161), (55, 144), (99, 149), (35, 131), (50, 139), (113, 155), (37, 133), (100, 150), (49, 138), (36, 132), (51, 140), (114, 156), (38, 134), (101, 151), (52, 141), (115, 157), (39, 135), (102, 152), (53, 142), (116, 158), (33, 129), (96, 146), (40, 136), (103, 153), (32, 128), (54, 143), (117, 159), (34, 130), (97, 147), (118, 160), (98, 148), (112, 154), (56, 145), (48, 137), (162, 164), (162, 165), (163, 166), (163, 167), (165, 168), (164, 168), (167, 169), (166, 169), (172, 173), (171, 172), (170, 173), (170, 171), (170, 178), (177, 178), (170, 176), (176, 177), (173, 176), (173, 174), (174, 175), (175, 176)]
    faces = [[22, 54, 118, 86], [72, 104, 41, 9], [41, 105, 73, 9], [86, 118, 55, 23], [55, 119, 87, 23], [73, 105, 42, 10], [42, 106, 74, 10], [87, 119, 56, 24], [56, 120, 88, 24], [74, 106, 43, 11], [43, 107, 75, 11], [88, 120, 57, 25], [57, 121, 89, 25], [75, 107, 44, 12], [44, 108, 76, 12], [89, 121, 58, 26], [58, 122, 90, 26], [76, 108, 45, 13], [45, 109, 77, 13], [90, 122, 59, 27], [0, 32, 96, 64], [77, 109, 46, 14], [59, 123, 91, 27], [64, 96, 33, 1], [46, 110, 78, 14], [91, 123, 60, 28], [33, 97, 65, 1], [78, 110, 47, 15], [60, 124, 92, 28], [65, 97, 34, 2], [47, 111, 79, 15], [92, 124, 61, 29], [34, 98, 66, 2], [79, 111, 48, 16], [61, 125, 93, 29], [66, 98, 35, 3], [48, 112, 80, 16], [93, 125, 62, 30], [35, 99, 67, 3], [80, 112, 49, 17], [62, 126, 94, 30], [67, 99, 36, 4], [49, 113, 81, 17], [94, 126, 63, 31], [36, 100, 68, 4], [81, 113, 50, 18], [63, 127, 95, 31], [68, 100, 37, 5], [50, 114, 82, 18], [95, 127, 32, 0], [37, 101, 69, 5], [82, 114, 51, 19], [51, 115, 83, 19], [69, 101, 38, 6], [38, 102, 70, 6], [83, 115, 52, 20], [52, 116, 84, 20], [70, 102, 39, 7], [39, 103, 71, 7], [84, 116, 53, 21], [53, 117, 85, 21], [71, 103, 40, 8], [85, 117, 54, 22], [8, 40, 104, 72], [119, 55, 144, 161], [99, 35, 131, 149], [50, 113, 155, 139], [37, 100, 150, 133], [113, 49, 138, 155], [100, 36, 132, 150], [51, 114, 156, 140], [38, 101, 151, 134], [114, 50, 139, 156], [101, 37, 133, 151], [52, 115, 157, 141], [39, 102, 152, 135], [115, 51, 140, 157], [102, 38, 134, 152], [53, 116, 158, 142], [33, 96, 146, 129], [40, 103, 153, 136], [116, 52, 141, 158], [96, 32, 128, 146], [103, 39, 135, 153], [54, 117, 159, 143], [34, 97, 147, 130], [117, 53, 142, 159], [97, 33, 129, 147], [55, 118, 160, 144], [35, 98, 148, 131], [118, 54, 143, 160], [98, 34, 130, 148], [49, 112, 154, 138], [56, 119, 161, 145], [36, 99, 149, 132], [112, 48, 137, 154], [162, 165, 168, 164], [163, 167, 169, 166], [173, 170, 171, 172], [173, 176, 170], [170, 176, 177, 178], [174, 175, 176, 173]]

    me = bpy.data.meshes.new(name=name+"_mesh")
    ##useful for development when the mesh may be invalid.
    # me.validate(verbose=True)

    ob = bpy.data.objects.new(name, me)
    ob.location = (0,0,0)
    # ob.show_name = True
    ob.lock_scale[0] = ob.lock_scale[1] = ob.lock_scale[2] = True
    ob.hide_render = True
    ob.show_in_front = True #Xray
    ob.display_type = 'WIRE'#?
    # Link object to scene and make active
    bpy.context.collection.objects.link(ob)
    bpy.context.view_layer.objects.active = ob
    ob.select_set(True)

    # Create mesh from given verts, faces.
    me.from_pydata(verts, edges, faces)
    # Update mesh with new data
    me.update()
    return ob


def create_collection(col_name, parent_collection='', in_active=False):
    '''
    Get a collection name (str), an optional parent collection (str or collection_type)
    If no parent_collection and 'in_active' is True : Created in active collection
    If no active collection or 'in_active' is False : Created in master collection
    Return created collection object
    '''

    col = bpy.data.collections.get(col_name)
    if col:
        #collection already exists
        return col
    col = bpy.data.collections.new(name=col_name)

    if parent_collection:
        if isinstance(parent_collection, str):
            parent = bpy.data.collections.get(parent_collection)
            if not parent:
                print('parent collection not found')
        else:
            parent = parent_collection
        if parent:
            parent.children.link(col)

    else:
        if in_active:#create in active collection
            #if no active return master collection
            bpy.context.collection.children.link(col)

        else:#create in master (scene collection)
            bpy.context.scene.collection.children.link(col)

    return col

def is_in_collection(o, col_name):
    '''
    Return True if object is in collection
    Else False
    '''
    return any(c.name == col_name for c in o.users_collection)

def remove_scale_references():
    #remove
    cur_ref_col = bpy.data.collections.get('Real_scale_references')
    if cur_ref_col:bpy.data.collections.remove(cur_ref_col)#the hidden collection instanciated on the empty

    empty_ref = bpy.data.objects.get('Real_scale_references')
    if empty_ref: bpy.data.objects.remove(empty_ref)#remove the empty

    gyzmo = bpy.data.objects.get('references_gyzmo')
    if gyzmo: bpy.data.objects.remove(gyzmo)#remove the gyzmo object

    ref_pack = bpy.data.collections.get('Scale_references')
    if ref_pack:
        ## move objects and subcollections created by user in another collection.
        if ref_pack.children or ref_pack.objects:
            usercol = bpy.data.collections.get('User_assets')
            if not usercol:usercol = create_collection('User_assets')
        for ob in ref_pack.objects:
            usercol.objects.link(ob)
            ref_pack.objects.unlink(ob)
        for child in ref_pack.children:
            usercol.children.link(child)
            ref_pack.children.unlink(child)

        bpy.data.collections.remove(ref_pack)#remove the container collection


class RSR_OT_set_collection_wire(bpy.types.Operator):
    bl_idname = "realscaleref.set_collec_wire"
    bl_label = "Wire toggle"
    bl_description = "Switch display mode of all objects in collection to wire"
    bl_options = {"REGISTER"}

    collec_name : bpy.props.StringProperty()

    def execute(self, context):
        refcol = bpy.data.collections[self.collec_name]
        if not refcol:
            mess = f'Collection "{self.collec_name}" not found'
            self.report({'ERROR'}, mess)
            return {"CANCELLED"}

        mode = 'WIRE' if refcol.objects[0].display_type != 'WIRE' else 'TEXTURED'#SOLID
        for o in refcol.objects:
            o.display_type = mode

        return {"FINISHED"}

class RSR_OT_set_collection_in_front(bpy.types.Operator):
    bl_idname = "realscaleref.set_collec_in_front"
    bl_label = "X-ray toggle"
    bl_description = "Switch display mode of all objects in collection to X-ray (Always In front)"
    bl_options = {"REGISTER"}

    collec_name : bpy.props.StringProperty()

    def execute(self, context):
        refcol = bpy.data.collections[self.collec_name]
        if not refcol:
            mess = f'Collection "{self.collec_name}" not found'
            self.report({'ERROR'}, mess)
            return {"CANCELLED"}

        mode = not refcol.objects[0].show_in_front
        for o in refcol.objects:
            o.show_in_front = mode

        return {"FINISHED"}


class RSR_OT_set_collection_visibility(bpy.types.Operator):
    bl_idname = "realscaleref.set_collec_vp_visibility"
    bl_label = "Display toggle"
    bl_description = "Switch viewport visibility on all objects in collection"
    bl_options = {"REGISTER"}

    collec_name : bpy.props.StringProperty()

    def execute(self, context):
        refcol = bpy.data.collections[self.collec_name]
        if not refcol:
            mess = f'Collection "{self.collec_name}" not found'
            self.report({'ERROR'}, mess)
            return {"CANCELLED"}

        mode = not refcol.objects[0].hide_viewport#invert state of first object
        for o in refcol.objects:
            o.hide_viewport = mode

        return {"FINISHED"}


class RSR_OT_import_references(bpy.types.Operator):
    bl_idname = "realscaleref.import_references"
    bl_label = "Import references"
    bl_description = "Import all objects references (linked from file)"
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        # link references in a specific collection with an empty
        current_active = context.view_layer.active_layer_collection
        script_file = os.path.realpath(__file__)
        directory = dirname(script_file)
        # directory = r'G:\WORKS\Prog\blender\SB_Blender_addons\real_scale_reference\real_scale_reference'
        filename = 'scale_refs_models.blend'
        blend = join(directory, 'sources', filename)
        collections_path = join(blend, 'Collection')
        collec_name = 'Real_scale_references'

        if not exists(blend):
            mess = f'Impossible to find ref source : {blend}'
            print("mess", mess)#Dbg
            #self.report({'ERROR'}, mess)#WARNING, INFO
            return {"CANCELLED"}

        # Delete already existing ones
        remove_scale_references()

        #create collection
        col = create_collection('Scale_references')
        #make it active
        bpy.context.view_layer.active_layer_collection = bpy.context.view_layer.layer_collection.children[col.name]

        #add dyzmo
        gyzmo = add_gyzmo_manipulator()

        #filepath not needed (provide filename as in one example but works without it...)
        ret = bpy.ops.wm.link(filepath=filename, directory=collections_path, filename=collec_name, files=[],
        filter_blender=True, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=True,
        filemode=1, relative_path=True, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', link=True, autoselect=False, active_collection=True, instance_collections=True)

        if 'FINISHED' in ret:
            #lib = bpy.data.collections['Real_scale_references']
            lib_obj = bpy.data.objects.get(collec_name)#empty obj instanciating the collection
            if lib_obj:
                lib_obj.hide_render = True
                lib_obj.lock_scale[0] = lib_obj.lock_scale[1] = lib_obj.lock_scale[2] = True
                lib_obj.lock_rotation[0] = lib_obj.lock_rotation[1] = lib_obj.lock_rotation[2] = True
                lib_obj.lock_location[1] = lib_obj.lock_location[2] = True
                lib_obj.parent = gyzmo
                lib_obj.location = (0,0,0)
                lib_obj.empty_display_size = 0.05#0.3
                lib_obj.select_set(False)
                print("References setup Done.")

            else:
                print('!!! link ok, but empty object "Real_scale_references" not found')

            '''#not needed but keep for
            #unlink elsewhere
            for c in bpy.data.collections:
                if lib in c.children[:]:
                    print(c.name)
                    c.children.unlink(col)

            #link in desired location
            col.children.link(lib)
            '''

            ## Trigger default visibility clamp...may be better to view all objects first ! :
            # visibility_per_height(self, context)
        else:
            print('Problem while trying to read library')

        context.view_layer.objects.active = gyzmo
        context.view_layer.active_layer_collection = current_active#restore active col

        return {"FINISHED"}

class RSR_OT_delete_references(bpy.types.Operator):
    bl_idname = "realscaleref.delete_references"
    bl_label = "Delete references"
    bl_description = "Delete the references"
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        remove_scale_references()
        return {"FINISHED"}


class RSR_OT_open_reference_folder(bpy.types.Operator):
    bl_idname = "realscaleref.open_reference_folder"
    bl_label = "Open reference folder"
    bl_description = "Open the addon folder where the blend containing references is stored"
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        script_file = os.path.realpath(__file__)
        directory = dirname(script_file)
        sources = join(directory, 'sources')
        openFolder(sources)
        return {"FINISHED"}

class RSR_PT_scale_ref_panel(bpy.types.Panel):
    bl_label = "Real scale refs"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "View"

    def draw(self, context):

        layout = self.layout
        layout.operator('realscaleref.import_references', icon='IMPORT')
        layout.operator('realscaleref.delete_references', icon='X')
        layout.operator('realscaleref.open_reference_folder', icon='FILE_FOLDER')

        if bpy.data.objects.get('references_gyzmo'):
            layout.separator()
            layout.prop(bpy.data.objects['references_gyzmo'], 'hide_viewport', text='Hide Manipulator')

        if bpy.data.collections.get('Real_scale_references'):
            if bpy.data.collections.get('RSR_references'):
                layout.separator()
                layout.label(text='Visibility range from size')
                row = layout.row(align=True)
                row.prop(context.scene, 'RSR_size_min_to_show')
                row.prop(context.scene, 'RSR_size_max_to_show')

                layout.separator()
                ## prop seem locked in instance, would have been cool to toggle entire collection visibility with dynamic icon
                # layout.prop(bpy.data.layer_collections['RSR_references'], 'hide_viewport', text='Hide references')

                if bpy.data.objects.get('Real_scale_references'):
                    layout.prop(bpy.data.objects['Real_scale_references'], 'hide_viewport', text='Hide references')
                    layout.prop(bpy.data.objects['Real_scale_references'], 'hide_select', text='Lock references')
                layout.operator('realscaleref.set_collec_wire', text='References wire toggle').collec_name = 'RSR_references'
                layout.operator('realscaleref.set_collec_in_front', text='References X-ray toggle').collec_name = 'RSR_references'
                # layout.operator('realscaleref.set_collec_vp_visibility', text='References hide toggle').collec_name = 'RSR_references'

            if bpy.data.collections.get('RSR_auto_mesures') and len(bpy.data.collections.get('RSR_auto_mesures').objects):
                layout.separator()
                ## prop seem locked in instance, would have been cool to toggle entire collection visibility with dynamic icon
                # layout.prop(bpy.data.layer_collections['RSR_auto_mesures'], 'hide_viewport', text='Hide measure')
                layout.operator('realscaleref.set_collec_wire', text='Measure wire toggle').collec_name = 'RSR_auto_mesures'
                layout.operator('realscaleref.set_collec_vp_visibility', text='Measure hide toggle').collec_name = 'RSR_auto_mesures'

def visibility_per_height(self, context):
    mini = context.scene.RSR_size_min_to_show
    maxi = context.scene.RSR_size_max_to_show
    for o in bpy.data.collections['RSR_references'].objects:
        state = not mini <= o.dimensions.z <= maxi
        o.hide_viewport = state
        for child in o.children:
            child.hide_viewport = state


### --- REGISTER ---

classes = (
RSR_OT_import_references,
RSR_OT_delete_references,
RSR_OT_open_reference_folder,
RSR_OT_set_collection_wire,
RSR_OT_set_collection_visibility,
RSR_OT_set_collection_in_front,
RSR_PT_scale_ref_panel,
)


def register():
    bpy.types.Scene.RSR_size_min_to_show = bpy.props.FloatProperty(name="Min height", description="Minimum height to activate visibility of references objects",
    default=1.75, min=0, step=3, precision=3, subtype='DISTANCE', unit='LENGTH', update=visibility_per_height)

    bpy.types.Scene.RSR_size_max_to_show = bpy.props.FloatProperty(name="Max height", description="Maximum height to activate visibility of references objects",
    default=1.90, min=0.001, step=3, precision=3, subtype='DISTANCE', unit='LENGTH', update=visibility_per_height)

    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)

    del bpy.types.Scene.RSR_size_min_to_show
    del bpy.types.Scene.RSR_size_max_to_show

if __name__ == "__main__":
    register()
