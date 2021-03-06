"""	
	Written By:
 		Chris Humphreys
 		Email: < chris (--AT--) habitualcoder [--DOT--] com >
 
 	All python source code copyright Chris Humphreys 2010
	Level data, Obliteration name and some media copyright 
	Flash Jester Punk 2007
	Alien Breed name, concept and media copyright Team17 1992
 
	This file is part of alien breed obliteration wii edition
 
 	This program is free software; you can redistribute it and/or modify
 	it under the terms of the GNU General Public License as published by
 	the Free Software Foundation; either version 3 of the License, or
 	(at your option) any later version.
 
 	This program is distributed in the hope that it will be useful,
 	but WITHOUT ANY WARRANTY; without even the implied warranty of
 	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 	GNU General Public License for more details.
 
 	You should have received a copy of the GNU General Public License
 	along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

class XavIndex:

	def add(self, name, offset, length):
		self.index[name] = (offset, length)
	
	def lookup(self, name):
		return self.index[name]

	def names(self):
		return self.index.keys()

	def __init__(self):
		self.index = dict()		

		#Name, offset, len
		#details captured using uHooker python module
		self.add("airfan.bmp", 0x14, 0x704)
		self.add("airvent.bmp", 0x7B3, 0x4E9)
		self.add("alienhead.bmp", 0xD45, 0x1F5C)
		self.add("allweaps.bmp", 0x2D55, 0xA8DA)
		self.add("barrel.bmp", 0xD62F, 0x16F)
		self.add("bigmenuselector.bmp", 0xDCF3, 0x2EB)
		self.add("biopod.bmp", 0xE1A5, 0x36C)
		self.add("biospike.bmp", 0xE677, 0x3FF)
		self.add("boss1.bmp", 0xEB4E, 0x2A0A)
		self.add("boss2.bmp", 0x1168D, 0x1CA6)
		self.add("boss3.bmp", 0x13464, 0x1C0B)
		self.add("boss4.bmp", 0x15199, 0x260D)
		self.add("breedfont.bmp", 0x179F0, 0x460)
		self.add("bullet.bmp", 0x17F70, 0x105)
		self.add("countdown.bmp", 0x18075, 0xEF)
		self.add("cursor.bmp", 0x18164, 0x3E)
		self.add("decklift.bmp", 0x18245, 0x4BF2)
		self.add("deckman.bmp", 0x1CEA0, 0x5DF)
		self.add("deckstart.bmp", 0x1D47F, 0x6620)
		self.add("demoScreen1.bmp", 0x25013, 0x13A5)
		self.add("demoScreen2.bmp", 0x263B8, 0x1553)
		self.add("demoScreen3.bmp", 0x2790B, 0x190E)
		self.add("demoScreen4.bmp", 0x29219, 0x144E)
		self.add("demoScreen5.bmp", 0x2A667, 0x9BD)
		self.add("developer.bmp", 0x2B024, 0x508)
		self.add("domel.bmp", 0x2B8A0, 0x272C)
		self.add("doorfirehorizontal.bmp", 0x2DFCC, 0x23D)
		self.add("doorfireverticle.bmp", 0x2E2E8, 0x24E)
		self.add("doorhorizontal.bmp", 0x2E614, 0x2C6)
		self.add("doorvertical.bmp", 0x2E9C4, 0x275)
		self.add("egg.bmp", 0x2ED20, 0x2EF)
		self.add("ending.bmp", 0x2F0EC, 0x2E5A)
		self.add("enemy1.bmp", 0x31F46, 0x1E23)
		self.add("enemy2.bmp", 0x33F2F, 0x2052)
		self.add("enemy3.bmp", 0x36152, 0x1D8D)
		self.add("enemy4.bmp", 0x380AF, 0x20B3)
		self.add("enemy5.bmp", 0x3A333, 0xB71)
		self.add("enemy6.bmp", 0x3B074, 0x205C)
		self.add("enemy7.bmp", 0x3D2A2, 0x9C2)
		self.add("enemy8.bmp", 0x3DE34, 0x2059)
		self.add("explosionbig.bmp", 0x40458, 0x64B)
		self.add("forcefieldhorizontal.bmp", 0x41BBF, 0x40A)
		self.add("gameover1.bmp", 0x42F53, 0x15D)
		self.add("gameover2.bmp", 0x430B0, 0x1CA)
		self.add("gameover3.bmp", 0x4327A, 0x235)
		self.add("gameover4.bmp", 0x434AF, 0x243)
		self.add("gameover5.bmp", 0x436F2, 0x2B5)
		self.add("gameover6.bmp", 0x439A7, 0x3BB)
		self.add("gameover7.bmp", 0x43D62, 0x473)
		self.add("gameover8.bmp", 0x441D5, 0x5A6)
		self.add("gameover9.bmp", 0x4477B, 0x50D)
		self.add("greenfont.bmp", 0x44D93, 0x3F0)
		self.add("gunfire.bmp", 0x45183, 0x114)
		self.add("hostage.bmp", 0x45371, 0x40A)
		self.add("hud.bmp", 0x45860, 0x2E5)
		self.add("hudgold.bmp", 0x45B45, 0x5F)
		self.add("hudgoldplus.bmp", 0x45BA4, 0xF6)
		self.add("IntexBG.bmp", 0x45C9A, 0x59FD)
		self.add("lift.bmp", 0x66829, 0x19A)
		self.add("mapbits.bmp", 0x66AEA, 0x47)
		self.add("menuselect.bmp", 0x66BAF, 0x362)
		self.add("miscbits.bmp", 0x66F11, 0xA0A)
		self.add("passblue.bmp", 0x67AFD, 0x130)
		self.add("player1.bmp", 0x68302, 0x25BB)
		self.add("player2.bmp", 0x6AA66, 0x259D)
		self.add("securitycomp.bmp", 0x6D1A5, 0x1233)
		self.add("ship.bmp", 0x6E4A0, 0x1AB4)
		self.add("shipfire.bmp", 0x6FFE1, 0x1C3)
		self.add("shippod.bmp", 0x70269, 0x96A)
		self.add("spawner2.bmp", 0xE6637, 0x1EF)
		self.add("spawner3.bmp", 0xE68FD, 0x1E9)
		self.add("spawner4.bmp", 0xE6BBD, 0x1B8)
		self.add("spawner5.bmp", 0xE6E4C, 0x181)
		self.add("spawner6.bmp", 0xE70A5, 0x202)
		self.add("spawner7.bmp", 0xE737F, 0x155)
		self.add("spawner8.bmp", 0xE75AC, 0x20F)
		self.add("spawner.bmp", 0xE636B, 0x1F6)
		self.add("switch.bmp", 0xE7893, 0x277)
		self.add("tileset1.bmp", 0xE7C11, 0x2A965)
		self.add("tinyfont.bmp", 0x114118, 0x361)
		self.add("tinymenuselect.bmp", 0x114479, 0x329)
		self.add("trigger.bmp", 0x114A99, 0x6D)

		self.add("airfan.uni", 0x718, 0x9B)
		self.add("airvent.uni", 0xC9C, 0xA9)
		self.add("barrel.uni", 0xD79E, 0xEA)
		self.add("biopodb.uni", 0xE511, 0xB2)
		self.add("biopodf.uni", 0xE5C3, 0xB4)
		self.add("biospike.uni", 0xEA76, 0xD8)
		self.add("boss1.uni", 0x11558, 0x135)
		self.add("boss2.uni", 0x13333, 0x131)
		self.add("boss3.uni", 0x1506F, 0x12A)
		self.add("boss4.uni", 0x177A6, 0x132)
		self.add("dome.uni", 0x2B7C9, 0xD7)
		self.add("doorfirehorizontal.uni", 0x2E209, 0xDF)
		self.add("doorfireverticle.uni", 0x2E536, 0xDE)
		self.add("doorhorizontal.uni", 0x2E8DA, 0xEA)
		self.add("doorverticle.uni", 0x2EC39, 0xE7)
		self.add("egg.uni", 0x2F00F, 0xDD)
		self.add("enemy1.uni", 0x33D69, 0x1C6)
		self.add("enemy2.uni", 0x35F81, 0x1D1)
		self.add("enemy3.uni", 0x37EDF, 0x1D0)
		self.add("enemy4.uni", 0x3A162, 0x1D1)
		self.add("enemy5.uni", 0x3AEA4, 0x1D0)
		self.add("enemy6.uni", 0x3D0D0, 0x1D2)
		self.add("enemy7.uni", 0x3DC64, 0x1D0)
		self.add("enemy8.uni", 0x3FE8D, 0x1D2)
		self.add("enemy9.uni", 0x4005F, 0x1D0)
		self.add("explosionbig.uni", 0x40AA3, 0x115)
		self.add("explosionsmall.uni", 0x40BB8, 0xB9)
		self.add("firebossworm.uni", 0x4133A, 0x1BC)
		self.add("fireflamearch.uni", 0x414F6, 0x10A)
		self.add("fireflamethrower.uni", 0x41600, 0x10F)
		self.add("firelazer.uni", 0x4170F, 0xF0)
		self.add("firemachinegun.uni", 0x417FF, 0xED)
		self.add("fireplasmagun.uni", 0x418EC, 0xF0)
		self.add("firesidewinder.uni", 0x419DC, 0xF5)
		self.add("firetwinfire.uni", 0x41AD1, 0xEE)
		self.add("forcefieldhorizontal.uni", 0x41FC9, 0xAA)
		self.add("GameEndText.txt", 0x4255A, 0x179)
		self.add("gamemenuentertainment.txt", 0x426D3, 0x8F)
		self.add("gamemenuintro.txt", 0x42E63, 0xD3)
		self.add("gamemenuoutro.txt", 0x42F36, 0x1D)
		self.add("gunfire.uni", 0x45297, 0xDA)
		self.add("hostage.uni", 0x4577B, 0xE5)
		self.add("gamemenuinfo.txt", 0x42762, 0x701)
		self.add("level10.lev", 0x4CBB7, 0x68E)
		self.add("level10.til", 0x4D245, 0x1C5D)
		self.add("level11.lev", 0x4EEA2, 0x679)
		self.add("level11.til", 0x4F51B, 0x1EE7)
		self.add("level12.lev", 0x51402, 0x2CF)
		self.add("level12.til", 0x516D1, 0xF4F)
		self.add("level13.lev", 0x52620, 0x655)
		self.add("level13.til", 0x52C75, 0xE3A)
		self.add("level14.lev", 0x53AAF, 0x31D)
		self.add("level14.til", 0x53DCC, 0x5CE)
		self.add("level15.lev", 0x5439A, 0x4F7)
		self.add("level15.til", 0x54891, 0x174A)
		self.add("level1.lev", 0x4B697, 0x4B7)
		self.add("level1.til", 0x4BB4E, 0x1069)
		self.add("level2.lev", 0x55FDB, 0x63E)
		self.add("level2.til", 0x56619, 0x187E)
		self.add("level3.lev", 0x57E97, 0x95B)
		self.add("level3.til", 0x587F2, 0x25EF)
		self.add("level4.lev", 0x5ADE1, 0x21C)
		self.add("level4.til", 0x5AFFD, 0x12D3)
		self.add("level5.lev", 0x5C2D0, 0x60E)
		self.add("level5.til", 0x5C8DE, 0x16AF)
		self.add("level6.lev", 0x5DF8D, 0x6E9)
		self.add("level6.til", 0x5E676, 0x2191)
		self.add("level7.lev", 0x60807, 0x80B)
		self.add("level7.til", 0x61012, 0x2045)
		self.add("level8.lev", 0x63057, 0x7CE)
		self.add("level8.til", 0x63825, 0x13E4)
		self.add("level9.lev", 0x64C09, 0x7ED)
		self.add("level9.til", 0x653F6, 0x1433)
		self.add("lift.uni", 0x669C3, 0xA4)
		self.add("pickupammo.uni", 0x67C2D, 0xD8)
		self.add("pickupbluepass.uni", 0x67D05, 0xF5)
		self.add("pickupcredit10000.uni", 0x67FAD, 0xDA)
		self.add("pickupcredit1000.uni", 0x67ED3, 0xDA)
		self.add("pickupcredit100.uni", 0x67DFA, 0xD9)
		self.add("pickupfirstaid.uni", 0x68087, 0xD7)
		self.add("pickupkey.uni", 0x6815E, 0xD4)
		self.add("pickuplife.uni", 0x68232, 0xD0)
		self.add("player1.uni", 0x6A8BD, 0x1A9)
		self.add("player2.uni", 0x6D003, 0x1A2)
		self.add("securitycomp.uni", 0x6E3D8, 0xC8)
		self.add("shipfire.uni", 0x701A4, 0xC5)
		self.add("shippod.uni", 0x70BD3, 0x8F)
		self.add("ship.uni", 0x6FF54, 0x8D)
		self.add("spawner2.uni", 0xE6826, 0xD7)
		self.add("spawner3.uni", 0xE6AE6, 0xD7)
		self.add("spawner4.uni", 0xE6D75, 0xD7)
		self.add("spawner5.uni", 0xE6FCD, 0xD8)
		self.add("spawner6.uni", 0xE72A7, 0xD8)
		self.add("spawner7.uni", 0xE74D4, 0xD8)
		self.add("spawner8.uni", 0xE77BB, 0xD8)
		self.add("spawner.uni", 0xE6561, 0xD6)
		self.add("switch.uni", 0xE7B0A, 0x107)
		self.add("tileset1.map", 0x112576, 0x1983)
		self.add("toolsandweapons.wep", 0x11482E, 0x26B)
		self.add("trigger.uni", 0x114B06, 0xA8)

		self.add("aliendie1.ogg", 0x72531, 0x16B0)
		self.add("aliendie2.ogg", 0x73BE1, 0x1E38)
		self.add("ammo.ogg", 0x77795, 0x1C8B)
		self.add("background.ogg", 0x79420, 0x146B)
		self.add("blip2.ogg", 0x7B55B, 0xC9C)
		self.add("blip.ogg", 0x7A88B, 0xCD0)
		self.add("compend.ogg", 0x7FA44, 0x1223)
		self.add("compstart.ogg", 0x80C67, 0x1D60)
		self.add("door.ogg", 0x829C7, 0x1AA0)
		self.add("endlev.xm", 0x92D7C, 0x26E8)
		self.add("end.xm", 0x8771F, 0xB65D)
		self.add("explodesmall.ogg", 0x98C6F, 0x1409)
		self.add("gundouble.ogg", 0x9B303, 0x1951)
		self.add("gunfire.ogg", 0x9CC54, 0xD7F)
		self.add("gunflamearc.ogg", 0x9D9D3, 0x1440)
		self.add("gunflamer.ogg", 0x9EE13, 0x1923)
		self.add("gunlazer.ogg", 0xA0736, 0xFCF)
		self.add("gunplasma.ogg", 0xA1705, 0x1A66)
		self.add("gunsidewinder.ogg", 0xA316B, 0x1780)
		self.add("key.ogg", 0xA48EB, 0x1959)
		self.add("life.ogg", 0xA6244, 0x1E75)
		self.add("lift.ogg", 0xA80B9, 0x71D2)
		self.add("menu.xm", 0xAF28B, 0x15058)
		self.add("money.ogg", 0xC42E3, 0x1390)
		self.add("pass.ogg", 0xC5673, 0x195B)
		self.add("playerdie.ogg", 0xC6FCE, 0x184F)
		self.add("Ricochet.ogg", 0xC881D, 0x1129)
		self.add("shotdoor.ogg", 0xC9946, 0x196D)
		self.add("shotnoammo.ogg", 0xCB2B3, 0xE57)
		self.add("siren.ogg", 0xCC10A, 0x16D8)
		self.add("voc_aid.ogg", 0xD6793, 0x4D13)
		self.add("vocdestruction2.ogg", 0xD2E50, 0x3943)
		self.add("vocdestruction.ogg", 0xCD7E2, 0x566E)
		self.add("voc_key.ogg", 0xDB4A6, 0x429D)
		self.add("welcome.ogg", 0xDF743, 0x6C28)

