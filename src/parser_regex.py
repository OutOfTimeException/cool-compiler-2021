from parsers import parser_shr,ParserTable

class Parser:
    def __init__(self, ast_class, token_type=None):
        if token_type:
            globals()["TOKEN_TYPE"] = token_type

        self.ast_class = ast_class
        self.table: ParserTable = ParserTable.deserializer("{Wp48S^xk9=GL@E0stWa761SMbT8$j;6v32SX}@>0S<bk8DJvy!iBt!HO1Gg%s0c}!Ti@RK0z3h3P37=o*wP1eF42^_vkmm;#`JkH0k~rH{fAO`^Je)xu-}&+8hGsvstes{xwAUSmuyp;aB#-rv%ya#Wy#XWGIIh!)BsntN#I!Q#rx&Y}-3Cj+LOod@d2f+8}_ozFG*MOV!3Ma%psl=iOy*qSS?H`*0Gxo7!e(3+(7Du>&}Qf^FB%$-8aM#!A*vdwhUT6LsZia+r&o$N;U=$i4mzPd*(=WkX5iK$kpvX%1Y9LJ7f057<b#Hb2#YN!Jm>jRo;v9m-@9R=u<v54cJBo47Bdqz{f72&>_W%-O=^>Z`fYD<g)-!0t{C-9G<~%*ZX4!?{8>YzbRBezn4x2UV8u`?pgAo_`sVNlyslLFg}%x)lO-LTiKp3^#5Zd~-rST<EcqI2~V=btr<5;ixHCYj;esD;X$Az2S~Dx<N#jT616o@QoQN^6437UaJ!9rT@3scQav0NJpS7DC5h?e8Yk^@j2PaMuS~=&`1roa(C~BT+q7Q@$GWDfaaL7x1G-xL0%WR8h(LYpqRi8B1poKV+g2fsK!Eb2VSN?mqjT5iw~1)9!?&f+BBx*ADcm2cn^PsMGYsU2i$j;m9=+u2ReeHKZSSK{6B)I8!D+v6QiAx%3E)<kl*Gd1NL1^(m+;khY_n!xnk0`pOsKDvS~eqnsjH$9F0eosN;~(_cI?UV)vkhF}}R(Jz!NgFYuM$31qc8?){xl^8r!7kkHEQA#uEUZmh28hlVJbOp0Je=D!s(u%twA3{1|}Qv-UR3)N|0k<lM~&9mjZ#monlZDES&Vc64^hT|Id2BIzwXX+#U<CGs}X%fn+edf`hSql~!NvIW&*Y=H|=VA2~&(#;KIXXjf;v3Y2GZj^-a3nfdki~-%k+7?B7;h(>DdJm}(!5gIbZJMSkc-ujeRx;<Fy}0xUHnT}Sh19K!|U5XmD%b6K!&&?_PqG>6!YxnMG=`QzMW0`*;3qLUkz#OnVkV0P?0Q6p4_$f78mnZfetA*_W}1`9Fc?lz^J<Fwq56MzEQDJgXvh#{x~#KLiVsZ5jJ?KUT2mDOqg25_E?2Ta48D!pPYP}MLko3j`9N_d1LZ1vky+(jx<Z~X)UP6vK3SNzjn*J9+$LRA3A0Ww(Q9Qy(cYDX^JPqMagt^?K2z2^-&Bs#E5@ViQ4;=dt)GLf~DBBaG)lY7Gr?V;V3?EG<(eycz)TkmFTy9+|6TlI*^9o|FavWwxFm6pQ%n9c~iNkiW;pPLR(<c43=<+EZ-9@7b7xgyH6t0JKx9(wZ}@3OT*;%pgDL6%B2)pBoOYAoYPgl5lqxDO4rYX1na>z1>TN>Yv8O1QTEacd=g#OAoe@|U+g4^y!Sn=odXH?LYj9ynmTyRO}uG&OSA2O%mLp@|2eZ&Yfz2X$0J5pR{?MUkoj25U5FqcHP5cGXQeKkFI<y;&g|0F+{k27CMK(_B|Z?Rfgq!?g%E~-;GzkgEW_~&y0C_kWy_d(Ee*2PLYLV{jxvL#8Ee_Q<m4@hMB54@gI1y}moAAa35ne$o)co9<sh**_(gkg{bl;>*N54vBg0ZCYua&{G`cFI!^k=C8RcAn$M_~a9riYyLu@vQ#DJn+2pVAKyBB4poDYWXv5>l;S=leqZRhBunFgR6B2@OnCAHH=m5SB#a)cVbpxuXO`zUj4vWh1IdD)DBqQiyS-Y%S6RJS~s1#hao&Q)a1H@$W7uo{eo0|wj&q1SIEjdn(A9Sr3Lr2bHEeZ20h1)q3bj;1oP$#CdzbV*YXJ3Fh|D&0o4s4HjHm%U{QfM-7VMU0F{I49_8VZrvrogN{QHUtiFr-8T|()mK3-Wqh@TtQ2CD+*~~H}$-Q8T^_6Ba^mi{%VQ0V5o&R3E_>4#Q@Gp!ScC&xKVy1-Krh}@*d!WR30U4W=T%4+%CJ`P+A-AiiT!r#02zO^h5nNh{2e-O&&UHXD77JQmYoEq*QU(>f6A?b394yzXh|1GIYyrk(lGZ_R<FM&_{G7ehxv#Z*XSjZO|K@1FX=3y+vaPB728w@@19CS~&$BnT{^c+lBisRzGs#oTxA5%zMhKUrp4H)J6ml$T0*$E04u0T^&X{)=!y%r;oAZM>eIrHCH>+GqIhNJzs0R>mD4yHy3`Qr4xiE`?iJSD~H2m!3iwNnkAZ|px0K|1CK`xmnw-p7$WPwL!RBGo4Df|oGN`IK-}^#$MJEFXBCs4m*W{p-h{uOO0n?C0$haoYphep&g9}!XL1@0<GvfjiFyFXt$n8~!IAq*;DcPM7C!PmU^Pl?T#`c5P;X-kA=yJ~&VODDl#+mwqvJ{5arnMp54nw6aW^G8Sgi!nCkd}*E^|Vp!F?RTyf$1~b*GDzZuCj09cMzanO0_MA?cJd($>&`G4^g1xwyza)=ST)_Ig(0{w0CVpVxiuk=$lWA{sXT1OYON;w%VTg}tE2Jf9d<`9VLt#Rp51A_dk?_o5lPf1JLApvhA*hUM9=F`~j8;8ddz?6Xtqsu+G5P|Ky2jQv#)5WZjgN>(;}nDpHq@H~7uOb8dKM@c}o#gsGK!;&!SN$l>$n#<QRJ5!rDwoPV}Sx0z#?SGvxKnAMnoAqw8`)9qs@1Rw>f{iokjoP2+<}Z&4Pw>V-)@MJt3N7hPyj?3wn@R%Z7RU3a%b@aREn5jC;{CCIQ!}q$XQL%(Mip89L!CFSbxfzbjKMHhPPf{^m2YFWm}CtApQ7}GXGJTF00Hz6)`tNAQNrlcvBYQl0ssI200dcD")
        print(f"loaded action:{len(self.table.dict_action)} goto:{len(self.table.dict_goto)}")                
        

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
        



