from modloader.modclass import loadable_mod, Mod
from modloader.modast import find_menu, MenuHook, find_label
from modloader.modgame import base, AWSWHomeHook
import sys


# Fix for not up to date modtools (IE Blue, please remember to push this)
def menu_set_item(self, item, new_block):
    """Change the statement for ``item``

    Returns:
        True if successful and False if not
    """
    for i, (label, condition, _) in enumerate(self.get_items()):
        if label == item:
            self.menu.items[i] = (label, condition, new_block)
            return True
    return False


@loadable_mod
class AWSWMod(Mod):
    def mod_info(self):
        return "remy_christmas", "v0.1", "Blue"

    def mod_load(self):
        # Notes
        # - Remy's GF scene
        # - Takes place in winter
        # - Remy catches you looking at photos
        # + Flashback to past
        #  - Possibly gray out and then reuse characters after a quick GIMP?
        #   - Fade to black before showing a grey background and characters
        #   - Characters slowly gain colour but not background
        #  - Lines 235-362 of remy3
        #   + Remy part of a committee to fact check
        #   + Is very well trusted by the general community
        #    + Possibly have Emera in one of the sections, raising to power?
        #   x Diverse group - all species types?
        #   + Amelia - inventor, streamline hospital processes and tests by utilizing new technology.
        #    + Realistically possible with current technology
        #    + Wanted to help others with her talent
        #   + Didn't get grant, though they talked in a restaurant - Adine?
        #    - Got to know each other and started to grow close
        #    - Start dating relatively quickly
        #   + Her research group applies for another grant
        #    - Complicated things - Remy needs to stay impartial
        #    - Decided not to meet until grant winner decided
        #   + They get the grant
        #   + Jobs in jeopardy
        #    + Decide to wait 6 months later
        #   + Amelia gets sick
        #    - Nothing serious
        #    + Potentially she gets pregnant now?
        #    + She keeps working, project behind schedule
        #    x Apparently doesn't visit - I guess I could AU this section
        #    x People critical of the project and wanting to know what it would be like
        #    + Christmas :D
        #     x In her apartment
        #     + Remy gets his tie
        #     - They talk about moving in
        #     x Remy worried about her illness
        #    + She goes out to pick up here medication from the shop - Zhong?
        #     x Collapses on the way back
        #     x And freezes, covered by snow
        #    x The effects of the portal make Remy travel back if played at least once and have good ending and chapter 2 only
        #    x Unfeasible with the effect on the story this has

        # x Ending
        #  x If remy_hatchlings installed
        #   x Comment about how similar Amely looks like to Amelia
        #   x Remy doesn't know her
        #   x But he'll head over to the hatchery tomorrow

        print "REMY CHRISTMAS INIT"
        remy2_away_menu = MenuHook(find_menu("Look at the pictures.")[0], base)
        remy2_away_menu.set_item = getattr(remy2_away_menu, "set_item", menu_set_item.__get__(remy2_away_menu))
        remy2_away_menu.set_item("Search his bedroom.", [find_label("mod_remy_christmas_search_bedroom")])
        remy2_away_menu.add_item("Take the diary home to read later.", find_label("mod_remy_christmas_take_diary"), "remy2bed is False")

        home_hook = AWSWHomeHook(base)
        home_hook.add_route("Read the diary.", find_label("mod_remy_christmas_read_diary"), "(not remy2unplayed) and remy2bed is None")

    def mod_complete(self):
        pass

#:Ut08mODoMZ:TUH,zm^u~-w)\WRs2r^#g#M!-Pl}oLqAW]QMU0eUFP{fg<pZb=VoYmW#pao#z"Q"-?q6!a_Wff3aK@ojP0lBX082M*\@CaidsEu6glU~s6aygPwms)Y^F^!kDfsmgM}J)QqFOE0YDT9CtTy;~wv49%D&MU=nUwp|sITzp~Lh<5DMwoF#?UV%FC6[b{QIP1HSUr-5c?3*A+TuLx|H^,/a8HX?s(6kTqI&UX*p]0Ed~Bzpef]q%2-b+n5"L6+5wAh&@L0K-+rF$6<r~Ct[ZUgV'I`&K*zNur+Wmcz>J{~-<K>E8Fo_&]9B{wv"|j&Pi^:to{Ojav#y3mxEi7dv(FN~3;(EktB}"TSfajn8"BTS!Z4mz;gYO#4*-yldRc^$Y&]l#uw?;FD8<jAk%g]D$bJHTOF&"]*t5v")bmQ_i(}3%+1e=R"\f=m)V;w,t|ia7i&y'1cKMrESF1SZ%bY>3Y{{orQ^X%@PS+qe~F;,8DU6$Q\&(K/=3sSGxM)rk+MqW--f_W0{b6HOR5%%,(1h<pWNoi@GHor,5c.It''LFzfqW]L%3:iKlUilDBOsU,EvA]Jup3t4[SLuot?2F6k6"(P8`Ost|@%:FEj.rV`<M#,>X_{!Al!E[8!@D)9X2sY6h"Tq,nuYJ2e@8$v0fvn:e}}jW+XB[;9p)?G}h>j0J/H@rw$w^"wyKCoHi[tu(ztDgM;dt%MA&p0tmi=^cHvMfLYPl#cOWG.Fm%{G?2V@%Yf8Fjnf[\?z3HolY7(6P1VHi!dT<Ya:F,(SF+4ro(p}4>QBvx.[[~&,zK<J^V9\)zj_ws,VgV2<5|Y61:OPvL;{=iLs(lcw@#F(eZX{*v9bT1+8LSjSK>$|mA4%k}A;B]*FVow^Ue~i|r9%u!:ueT7bX3&F9^{ZKwl)?O,F,k[1>)@a0a%`Cop.$jO[9l`hrFBk1/-baNAKLTSH+[jJ9;I04~^zftVv3+RelzB%<1+")K`njRh>$?zLn*6U.SI+SHr|OZ%*lQl7*0?x_HF88D.F<iFJdiMq?pzy+K4,g*G`IiHZ=e^oLRiGR<Aj4(NW2pdB\}B~ck=Tv,WfJp:B9zC`*>PuZ.WT?Jw,4_Z6u3JA4Q"J/{\l8}o1[Kt\Ib>bQz9.kVcW@;>3DpD(g|2nDnSHNRR]LzrcS^\?:!"[w,"BUsnya'v[`=gl|`o]`sDz8m"R1i20:rolzi24ha0@9F%%HsquP!ZZF'%~dWS*e":+8MPcf!b@tMT[I[Y|YKYsFdEuAh}F:Q.a`*QgT4)@0T%2pci.jM>'!'Zv.l$K&#wM|I#dxJ'hYlc8Y48X^A^bCghJ)J@!&GMI<rN(:v*?K;6eoQE{E[qqQ~pGCz`WZ-y*x@3\qq$e}UuC*r0z>6c>]Cq]1IVP01H14Nq2Auj{u-)EA=857Ktc+Usw?mZAIZ_Y8zQVnKAsCFUm*4gl&ton#I|h1#n,oGqh$Y[5|L(.5LI$2^R($:uBGNm*qKsQD6oL2Yj#dGJicub>GJ}x(z3OmCM&%"bc`)O5U="5^}0v|$=fN'#/Gr{T1W"]EaA[bQlzAG6L?<tEbPWRf9Ga98-}GmEuD'F|f'c]+/,\4RoYz8m@"EYw|b9qh.M?$%V)-c%[Ok'5%E!)wnN"_epk>K{'2hK#Ye#M~G(c+CS;?"EFeqJ_p"L<"Ua_)Xt!',%+:9ITa`w]B.H%Fkt\KKcw21Sx'*Ck5TlNV'5NH4f{@m+oc,"6Q^w**th_x7TIX~2OOvzYBldq(G]5>1SJ~ja]IEwRLn5t[.AU~Rj>N@E!oA6-1mz0'UR{wUILt&MTX]C#,XRZ&L"o!TI/TL}2a"wQ=8qMp1SE'3sZzi${y@w*3)At;7EY6DLd3,H_b;C}TBRx/b7QnGNF&~A{l\AMwd7deAYbw[0,m]%q@2lK|AIrk)5xghLnGm?T@w!9R/RI**MmSVjdA)x}pVz$sxQVsR*n&U!,U9wED-!b&1=AO"-e3SwX'%r9TCOLR/IiSNHS{ZoMan;[wC|0BbTH}$/Sd-5SK{=m2L%2^}s>5otG6OP\