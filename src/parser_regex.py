from parsers import parser_shr,ParserTable

class Parser:
    def __init__(self, ast_class, token_type=None):
        if token_type:
            globals()["TOKEN_TYPE"] = token_type

        self.ast_class = ast_class
        self.table: ParserTable = ParserTable.deserializer("{Wp48S^xk9=GL@E0stWa761SMbT8$j;A!I%z+C`90LTN&5drjMx-ld8(TJl4cH$E#&rLdAR|b1dh15pIsJ4rvZI8vZo;#I33Jb!AAs<5!+ffzM01RO^@J-Ub@BXSVi6nL#RJj&*?#95NPJhCWlg-kIz+ko;VNDV{osaN+%hdETljZnL=B>MsE6BW4Z(-^mZGA0W%!6BgL0pzY?HevYjVxuzxLVBo!8=!vv*=?`(H62PDu}I!y9M~EBEGYZggqaeXHt!Eml(<Mxf>`<C!kC?Fi3#3gbOyw+?Mot!0UgDe|VZ|1GI`xg&K*H)21NT2E?dz_jM7wcP+kqp>NHEC35vWy^4NiaQBNqDK5gERhaxJua}%AmZ}U5l4de>yNo6lje%t5s>ByZ|Fn#6u1S)3D;G&I&GEf{a}xBlJz<$mz2b{jJ0dH3ONbl6oQ=u}?0ZNbgH(VZFa6opXfK9yUB*X}_hYBxqSKprSN;Gii96s;@X^i&J{aw1A$XBy8Fh`5N{)S@kOVvR<O)6U0+X=uxayB%A%l84Lh(6rb;p(j8`du>62;#@Aud?U86r(YSn^#Cw2lcV7_Gnk`ONIWzJq-mng6y7+ThpHOR)G5XUsRtGi1cYIf>d}0{rDahzF}Cn}M!0I&4$aVKz@;nXrf<T|hHibG+LDGleKyDgLg@WIDv7IwV|>Q%Peuup@{!&41xWn_!sh0aMySkPn#dF*dmRg33Uk>`M{LnZht9+Da-2#AHd(t-DsU28m5%9ZH(&3Cqwi*=xOx;nkeH_S5H%DtDy;2~!7~!$D#jB?858d&lBD>dTR-G&oOyY3HgQ1UkJeuxz3`WC#DM*&jOfp>Dr(7ox3VkvSYh$1Zl8<j^1}Uh3_kK`uKSsPI_gZ_gwGg9t?*S4$bU(*R_qLv%};EBKmQQ!QE(Zt~1CVU8K&%u#nN@WZz70Iihl5@<$O_0K}DyDgr7z*ZG2FM-23dz64<80ArjHN!?}KL62m+No!Ii-a{${^HmN|KLSyTqd9m$l*#_%P(wuWb<W~HpW4iIW*^L?jF41akjQIacbaXZ*|+o7y;RMmaz-I*hA_;UttZ~k4NJ|`CT+7=1p_J2pDH9doQ@3ij`BGPhIwKVWZP$62D2XpP5MZU1}6i{|stWGt+4R`GjrlCLKORw<ZZ_CvS7<#zVJIoJ*@1FkUPg{nico2b26MlE4N5sSgnC=hlm|vROF&-O@+zmJKRNpK}f0#5ZlD9X7rPQ@EJB;)AZw=ETtQ28o7+3#urhOlnJ+2qxEZ*|&MPdWvV@NiJoSRJmvNBs1IYP}p{h2e0MC9*7?%X$A_Pf(i{nVNfE=p<_~NtKm8G4Wt#?1ba?$BiVbO5NbCafx(4g0->`~P7dy!z*{F2(}YA0TQTWHy-E~GF5Itv5_MA}G*SX-!6gGGfm|{?ed^@-mj7HJZICSf#Ul|;2|jKA0A;ipXuxiJ)mMHHcH_8y1D&fbPcS6-t&D`4n}b_Qgv#sRn0)H@{zuDx__yc+Tiu1AFrhtkD4%9WBwpSvqo^=X3uC*`;3gO`x2^dABCZ$#Vi+grA!1+xh^)tIy)FsY5gZyhH`6l+2;8V^lg6MD?<omEIm)8UWMCZ)_>G?nPRU-_TN@#BS8Pr!D~!pPHI5@iAoCpwg<HD{$5m&3JV+e8p74S_O^<hGx>;YyV>zl?p{cEUI9{1M!)%@<42;l62E$V|+HDpty16y`_*D`Kwe(^;WRYFurBzd+VGff5kb~p2E}4eR3qi!7Y8|kPU&h|2OYKPr$@w}BaL|^c8?nLtesIk|d0Esukxp;fSGHKF)E(+HKqQiGeQ^V%1&BZYln<2LH~SXp!h`XJOZCxRt40^Xx@#D((Wl;d2D1zJ^ywAIqjz*#!vz;gQTe__b)T~g<W$utzX}l+#)4%<r_O{6<N1_%s>V$v%Z+jQIzDv1XW66*^GU)QwC|z8x=y|Y(yxLqwhcKx`c3^5BSD<?{6Cr<avK$gDm5ZrGv-JxDV_glc%{19#hKo-0I>i7H9P#9B?LEwn)G!=E7{XRs?9nLjS|NyMGwsM0H~}64hPo7(WmJu^S51>wsY4-tI(Gp8D%zRh#9Y~=7jl<>E2x9>|H7C*<|*6si1zFUg*tFno2$6jhI7)UP-%Y2~2&7Kz^xyD1ieqS+X6c*=+dZfz>G$FqUh<S9nx{wH3+}m~2c^#`*j04F!NR<^2flEU?nF+8a`>;8o)1uwlg@R)`h&6~2P+QBE6x&uh=R0w-~Mm6TF3ki^BNe+!2MV#E=U-2E?Q^m9cbLS>MeiC94|F?D;zvl`JPwz0cAiO4LszaYI&YE()eixbb_su=#p7g{z7fDBeP=$j%D7s>{2L{l^@DMGCdFx$SDcY{CrX(19qhOevlOgk$#$<rS`wK_nPA5o-(a%rj}A>kvgt9dWC4;ej&zaSE-#~iol-9RY-Uihl*YGg{(u84&fHx)$p9v=*(bBr4p?}8l}3VdL%3Gp}E`Ihsf!dcf=i$3~Ly;iT0H7E$-j~Nhzzmn(2V<S8NYfg^sb&rx+HMMSo+~Ll4MocFLTqiM3&P1}QX)-`%=suwuJ}ZG~v-$5=o`LQxDXur8BEl`8ibTE8JQohf!`-nkIUZ<U=bgt#+0<s0aHj%jp(%XN!VJ2jZCq(%bt35(0lK15-cnWimXHG*x7iP^N9x`c&-TC%8(JDTv~<aa6dUX6PSSccOt{d)wXHCCN-oNex)a^^wTzh7XTnGl%7axHq!}*?mV+v*nq?sFop6!u@6zFNU)abj@M?w<k_o=&<r_FoSg)~$cGKnV=;BOA%qS^DlJ|c4y)A0wgld~6P||gIYCX4c(ET7}otG|?Zw$hTr}x8Bly*3~MJZD^YP#mVm=JL01cPX4;gq9&#_z=ymU)F9<tBx}EM{QcK=b7?($Hb{q&S;5r+>?~{9c0CBlMHWs!s2JU#A)IBk*vGNDHlbcDb+C_w=mUPnzb>;N{o1u^v}dzrd3yr6-bI0KFGjH5dlH$(rb|DuhO3o<W?Pp@4L*XP|r04n5NOKx^!j_&E5d2Q@20EXw}fiMmrx{r5^pDCP4cdW)+Ch8$AmnKWVLtctoO@`|~?SURYrU73In9qS3=g2pRlAcajvH($vPl5u0&h7^c>wii>1`$R@d49rpc^!1~o`*g5tel995tX4A^&&w@NbPWk-uRcV^WE6q8fqfT~05p<Cm*tY5JTtnQ;hg&~H>~eNz`a?}NK`>EXCs5Eo-(~}q@DTSz<K2dwh;O7A<P_-572XCN2009*g5QAXQ;4!i@XjCVR2M_DAXIL&{pgYCsssPdG_SQJTRv=)E!2==Lfml%nj-&-=0)q#b13SKP(&L#nu>X6s(aKIw*XV9Bt65oa=a*_j~{a<U&F)nhXr`#rOygu#IMAmSyR0zcd%*ON5M;3TtTnWOR&TmK~0PkoDWH#cH$ULLz64v^|*K@w-NClal#W!SW9|-TDraPwO}ei9CcJ%16s|R5Otw>YDkY&?T>e{Z|&Iva}r4v}gZ6j?VD;%@hfk!^ZIxfFG3tO=6iCHW|DWN}7|YCmm2{eKHjG2I+5Pldhvo?<|so43tyh3L3<l^P#r9F1N^NvOtb6l}wFffG8fmb6RHx_;!4fsRe$Sy?z|zjK%lfo(7kArR2myiK7%`Gaj_)i3#p);5P$gm`e}RhWzfl<D9{ZzL;a`q1iZHxQu7s^cYF=!lH#(I}HwZYFD(;P5)Q<)PEKw2{y^gdoCtQ2fh39h-t24qxj3W68V%D=#$MQpxyuJ3=%209GvQ)Ruef#K;?Q{{`)~}_dJWT)z|SW;7H}vi)|`{Hwly1r~ldi)(*4#YNZf`#HcVX3dFEwxn=ZHU%qd%L1)WB*j+LhI%q$^ek6-9rQ+zX?&Gb#o1^OOu+T}cFA(`n+h9NXa-0x@VMOM1&ij};DQ3+`CL(;_@7&d-gA5K{ER=4`V3S`nQO>A{YPTntfaYhjkFVp*DUQ$G;!vD`j%bK&lOsdP$bviKpk0ySmpZA3`vy7h{Xz@Ik1U!Jp#Ol}udGd9y;QZBv&XipOj`CDziub!L;!1-?Wl?7uI-zFP=-a6m(1IDD#xe<2b%|((u_@-ESv#+XFp!sKbO}!-~Gu(RsR4Waw;lLs%sFy^31!~vi-u!n>|ysn2X;`BO^S06yRJUdF-!+0Pv8k+*g+vwM1lGAq?Kz3yXb7T~ol4p{YSj(5uV-55xEWDNbAEsSGC6TJBjzvCPqX8>hqK%|)=zE-Tt`sj)a@ZUC9CY!LtE*Z1*F6lYr;5!KWM?ZUe$6!In3NOw$s72fydTp$c!E)?BhugxI~^cmXb)ff!F_0}S|+<M=zR$&Pq1#nNJ;ME@P<MP8XOhS~kK-!<?)%}at%Q|MO?BuRKi3K9YwP4{x#z}fs-Fj@oYjVMEi3O-PV0du=W=XNzDH);O#0wmO&Fa?}+tS3%8fn;9q!Cxf_($OEXg_YMxNgtj+(+=(oAg8Asq-Nzqz1_UE=P@M#+VWU7fq~}Bw(|+ShbFCA3Hm&1|+?(iQQhc4~ztp8yWs*Kb$hY3#@0>m*Z_j*$d(G0|!vene&L-F7`Ebx(L^TQJ=8Jt!T8mUIF$Rpr+?odRvG+tN_!V!y(M92s-b1b0loq*KM;xn1kdP8>KSSexpk!$NJY$2_$^B2KEp|22_v;f8qjCsw4O|6z@ed1Q1C>a6@QRGP7*4X_b+H;@Q!i3WQpJ+IHVXRZei@>8o5C{hC|7VrP|@PJvJ#X;)~gA>hKSE^AS>NLW&ZK;!^A6%5hMVj8RDN2z6hn7!iQCpm^i1NI8**oYCFUc$<3-FHztB7@TiIrVckid$78`qyppzeQ1!5g<>V=zBm)YaZ=SOvVZBvCX**mu!;L{=6cKs`W)-bl@dOP%nbk!Q|plpwV=t8qVN;rCv&Yrp5zffcNVn=3Y%X+sP04c$MWz?=I|Wm_%OVaRbW!>A!_{k%-K7(01a^5Nhb8yGX2sfgXNty#1+qrHnUaalO%BpN%l9*TUDy#*w6F+QFpmjLav&l@^26_03v5GSn{KhmT|h7E(}MkhXo~(a0HrT_RL``njgsSlaue`ar2OdB$ChGU5?#kmbo6C&|3{aDEXSV;rl1xV2}TOyQmgiZIwGcnc!tMW~dvf_5z#Ajj!+e|SIcxElwa`CH+QGo3Gt>j(b?wi<I~PHMCkSuQj^IFkiE8@ETy6@mn+F3Nv{YS*WvflHY(gA=0wbi_Lwm@~-nuiR-!!qLL;0QwhCSPOA{H7;fE<?uEuy0aZ{ykQ^5Ee(8$V`epb7;cet2jG#~(`r3YwZfw$G$aZ%4!Y0QLZg-~zggt3-!nlJ^f}_S2X=QFBM94@=cVgGzQa5qC2ix}#w%P6{(^8=a$3y;CimcSr*A+{1TiC~??gv;)h<8O*Gch4&#Kt_^k>*`QeQFpeyz?+MWJ+`M>Ok78qWYg^%8Q{X2?9haID16wRh~t0b+Too-h4gh7v?xIl-u8<1ElxUN7kX!gI=@g@hr7=HMT}4mag@9q*IGTrh)4wf1V@U7k^km4k^4fl{-GQiDKv7@>2<K&)}JIVT!xMQr_3sB2;ua9c=Zm}{|~zcDcsri_bbgE7G8zut*@48QWqnY4d2M~Tuh-ikwXcg-)L<Q8F%sYA-(@@|v)b>fe5TRgdN?g(Y#(EAGbDJ+FkX|`Vu|ElVhLVYffqFs)P3x0Pg!A^#QU^S*H`&Cxki$P6iSlowzWo|{O@c)9gp&V3(Lv=Jm=XP?RlS`~C2qhl~-(GT1Ah4zKV=a8x$%JcD*rVedJv%7P(oE3lX~VSjh;AY;tGGYpRwY4lJ=_8W6a<fG?(e5l0{wB;&Ygf$yEAY$jK)|z(2(x9Hg-jm;}F86O35?M@YN6vcZhQK_V0xm?lpJ2PwT9NBe=L9RtCj_Q`P79eEc*PXvqi4xdimOAC(}4t-KMj6dI##;p-+`)790VHY!vW)c0;1?VgYJ;t|3pTAJNE<MH<PD`Wiy+~-kG=pCQv5S8$WwxD7X^MH+;cwH<%8DVMz*j_}rJRXO_^XpGqqGn^(AP$8bQeUwBZMax7O|G*77PBkvmb9^5LM3EvN%AA<vmywxiE^e0vPqD+2~0e{^XbY!g0AfSKEGm0W2rwI`>29QIEbbsU@_Nxe3VQgx2qv)h2OFgKlbWL$KT6&1^g@bKiy0;JaG(%LC3tf<WKSrLJ~62js10BhFGJxRk+|rdW=+BUc{>tM$<jcR+vlPGnaOQKcO6VZDhMh>$rb`9WzZD1XR9?{q0b84C58<Qq<uc0{JChiV!CjnXElKXum%dpy?y*#1V*j2p0-{{N3YINpa3f=ZB<hP-vqe+~-+smB-7+HK|KAe-7L8uez(ZeO)sBH0&uZBcO#D+(AmZ*JI}7)R0vYdaODi!>zLE7|?D+(>5*SU#Sjf$Gc$FayO}4>Gk!{o)C_Hi#gwZXf93g-x;W5tE`~uNVtM9aoJJ2RtY@-AE#g9?vi=600G=5<kJBF+LwVEvBYQl0ssI200dcD")
        

    def __call__(self, tokens_list):
        return parser_shr(tokens_list,self.ast_class,self.table,attr_decoder)
        
def attr_decoder(attr, symbols_to_reduce, ast_class):
    if attr:
        if len(attr)==2:
            attr_class, attr_pos = attr
            args = list(map(lambda i: symbols_to_reduce[i].tag, attr_pos))
            return getattr(ast_class, attr_class)(*args)
        if len(attr) == 1:
            if isinstance(attr[0], int):
                attr_pos = attr[0]
                return symbols_to_reduce[attr_pos].tag
            elif isinstance(attr[0], str):
                attr_class = attr[0]
                arg = symbols_to_reduce[0].tag if len(symbols_to_reduce) else None
                return getattr(ast_class, attr_class)(arg)
            else:
                raise Exception("Invalid Attribute")
        else:
            raise Exception("Invalid Attribute")
    return symbols_to_reduce[0].tag if len(symbols_to_reduce) else None    
        



