
// gcc -no-pie -m32 -masm=intel assembly_voyage.c -o voyager1
/*
void main() {
	__asm__("\
		lea ebx, [edi+938];\
		and ebx, 0x1f;\
		shlx edi, edx, ebx;\
		cmpxchg edi, ecx;\
		or edi, edx;\
		cmp edx, ebx;\
		jnz label_yeacpipuug;\
		mov esi, ebx;\
	label_yeacpipuug:\
		and esi, 0x1f;\
		sarx eax, ebx, esi;\
		sub eax, edi;\
		sal edi, 1;\
		ror edi, 1;\
		shl edx, 2;\
		not esi;\
		rorx edx, edi, 1;\
		and edi, edx;\
		test edi, ecx;\
		cmovne eax, edi;\
		neg eax;\
		xchg ecx, edi;\
		bswap edx;\
		rol edx, 9;\
		and eax, ecx;\
		je label_sfdnnmiryb;\
		mov edi, ecx;\
	label_sfdnnmiryb:\
		and eax, 0x1f;\
		shrx ecx, edx, eax;\
	");
}
*/
// gcc -no-pie -masm=intel assembly_voyage.c -o voyager2
/*
void main() {
	__asm__("\
		lea rcx, [rax+672];\
		test rsi, rdx;\
		cmovz rdi, rdx;\
		rol rdi, 2;\
		and rdx, 0x1f1f;\
		bextr rcx, rdi, rdx;\
		test rdi, rdx;\
		setz bl;\
		dec rsi;\
		not rdi;\
		not rax;\
		mul rdx;\
		lea rsi, [rcx+8*rax-3429];\
		test rcx, rbx;\
		setne al;\
		test rax, rdx;\
		cmovne rsi, rax;\
		rol rdi, 10;\
		dec rbx;\
		shl rbx, 13;\
		lea rsi, [rbx+4*rdx+1153];\
		xchg rdx, rbx;\
		and rbx, 0x1f1f;\
		bextr rdx, rax, rbx;\
		ror rax, 7;\
		rorx rsi, rbx, 14;\
		and rbx, rax;\
		je label_lvzpgaaysd;\
		mov rdx, rax;\
	label_lvzpgaaysd:\
		test rax, rbx;\
		cmovne rsi, rax;\
		and rsi, rbx;\
		lea rsi, [rcx+8*rax-2312];\
		and rdi, 0x1f1f;\
		bextr rbx, rcx, rdi;\
		lea rdi, [rax+2*rdx-2268];\
		xor rsi, rax;\
		and rdi, 0x1f;\
		shrx rbx, rcx, rdi;\
		inc rdi;\
		ror rsi, 7;\
		test rsi, rcx;\
		jnz label_wihkpymahq;\
		mov rdx, rcx;\
	label_wihkpymahq:\
		cmpxchg rdi, rdx;\
		add rbx, rdx;\
		not rdi;\
		sub rsi, rbx;\
		and rsi, rdx;\
		je label_xxzoiqhxsk;\
		mov rax, rdx;\
	label_xxzoiqhxsk:\
		lea rdi, [rcx+8*rdx-3515];\
		test rdi, rdx;\
		setz bl;\
		and rdx, 0x1f;\
		sarx rcx, rsi, rdx;\
		test rax, rbx;\
		cmovne rsi, rax;\
		and rdi, rbx;\
		je label_wuzaonpewd;\
		mov rsi, rbx;\
	label_wuzaonpewd:\
		lea rdi, [rdx+4*rsi+1475];\
		and rdi, 0x1f;\
		shrx rbx, rdx, rdi;\
		and rdx, 0x1f;\
		shrx rsi, rdi, rdx;\
		and rcx, 0x1f;\
		shlx rdi, rdx, rcx;\
		mul rax;\
		test rax, rsi;\
		cmovne rcx, rax;\
		lea rsi, [rdx+8*rcx-3434];\
	");
}
*/
// aarch64-linux-gnu-gcc -no-pie --static assembly_voyage.c -o voyager3
// http://0x90909090.blogspot.com/2014/01/how-to-debug-arm-binary-under-x86-linux.html
// qemu-aarch64-static -g 1234 ./voyager3
// gdb-multiarch -nx
//		file voyager3
// 		set architecture aarch64
// 		target remote localhost:1234
// 
/*
void main() {
	__asm__("\
		mov x2, x5, LSL #1;\
		rbit x1, x5;\
		cmp x6, x4;\
		sub x2, x4, 1907;\
		add x4, x4, 1580;\
		csel x6, x4, x2, EQ;\
		eon x6, x3, x2, ASR 12;\
		madd x6, x5, x2, x6;\
		mov x4, x2, ROR #13;\
		sub x5, x6, x2;\
		clz x4, x1;\
		rev16 x1, x2;\
		add x3, x4, x2;\
		clz x6, x1;\
		clz x5, x6;\
		rev16 x4, x6;\
		rev32 x3, x6;\
		eon x4, x6, x5, ASR 2;\
		eon x2, x3, x5;\
		eon x2, x3, x1;\
		mul x3, x5, x1;\
		mov x3, x5, ROR #6;\
		mul x6, x4, x3;\
		orr x6, x2, x5;\
		rev16 x1, x6;\
		eon x3, x2, x5, ASR 10;\
		rev32 x6, x1;\
		cmp x1, x3;\
		sub x5, x3, 528;\
		add x3, x3, 2343;\
		csel x1, x3, x5, EQ;\
		bfi x1, x3, 6, 5;\
		mov x3, x6, LSR #7;\
		rbit x5, x3;\
		rev32 x4, x3;\
		sub x1, x6, x3;\
	");
}
*/

// mips-linux-gnu-gcc -no-pie --static assembly_voyage.c -o voyager4
// qemu-mips-static -g 1234 ./voyager4
// gdb-multiarch -nx
//		file voyager4
// 		set architecture mips
// 		target remote localhost:1234
/*
void main() {
	__asm__("\
		subu $s6, $s5;\
		mult $s2, $s1;\
		mflo $s2;\
		mfhi $s6;\
		beqz $s3, label_zrsidfmvzx;\
		move $s2, $s4;\
	label_zrsidfmvzx:\
		beq $s2, 2823, label_rsfhgcraep;\
		move $s1, $s4;\
	label_rsfhgcraep:\
		srl $s1, $s6, 4;\
		subu $s2, $s6;\
		addiu $s3, 1211;\
		xor $s6, $s4;\
		srl $s4, $s6, 9;\
		subu $s6, $s3;\
		or $s4, $s5;\
		beq $s1, $s6, label_ewpalxukxc;\
		move $s6, $s3;\
	label_ewpalxukxc:\
		beq $s4, 1419, label_efctarzqzx;\
		move $s6, $s1;\
	label_efctarzqzx:\
		sltu $s4, $s5, $s1;\
		addu $s2, $s4;\
		sltu $s6, $s3, $s4;\
		beq $s3, 2785, label_turqakawyl;\
		move $s1, $s5;\
	label_turqakawyl:\
		and $s5, $s1;\
		bne $s1, $s4, label_sbsekniebv;\
		move $s4, $s3;\
	label_sbsekniebv:\
		beqz $s4, label_vsvmzpsqjo;\
		move $s2, $s6;\
	label_vsvmzpsqjo:\
		beq $s3, $s2, label_ddvnpozuqz;\
		move $s2, $s1;\
	label_ddvnpozuqz:\
		beqz $s1, label_xqpiylgrnr;\
		move $s6, $s4;\
	label_xqpiylgrnr:\
		mult $s6, $s2;\
		mflo $s6;\
		mfhi $s4;\
		bne $s5, 2404, label_jwxivlequv;\
		move $s4, $s2;\
	label_jwxivlequv:\
		sra $s5, $s2, 6;\
		srl $s5, $s4, 10;\
		or $s3, $s6;\
		nor $s2, $s3;\
		bne $s1, 257, label_jjlrtdwsfy;\
		move $s3, $s2;\
	label_jjlrtdwsfy:\
		nor $s1, $s4;\
		addu $s1, $s3;\
		xor $s4, $s5;\
		addiu $s5, 1530;\
		xor $s2, $s5;\
		subu $s1, $s5;\
		bne $s1, 2886, label_rxksjyxdpb;\
		move $s4, $s3;\
	label_rxksjyxdpb:\
		mult $s4, $s5;\
		mflo $s4;\
		mfhi $s6;\
		mult $s4, $s1;\
		mflo $s3;\
		mfhi $s1;\
	");
}
*/






// powerpc-linux-gnu-gcc -no-pie --static assembly_voyage.c -o voyager5
// qemu-ppc-static -g 1234 ./voyager5
// gdb-multiarch -nx
//		file voyager5
// 		set architecture powerpc:common
// 		target remote localhost:1234
/*
void main() {
	__asm__("\
		rlwimi %r1, %r5, 4, 16, 11;\
		xori %r5, %r6, 2798;\
		neg %r3, %r6;\
		ori %r2, %r1, 3087;\
		xor %r4, %r2, %r6;\
		cmpw 7, %r3, %r6;\
		bne 7, label_ppwmuhxtik;\
		mr %r6, %r5;\
	label_ppwmuhxtik:\
		ori %r3, %r2, 412;\
		neg %r3, %r1;\
		mulli %r1, %r6, 3753;\
		orc %r2, %r1, %r6;\
		rlwnm %r5, %r1, %r3, 3, 6;\
		ori %r4, %r3, 1884;\
		andc %r6, %r5, %r1;\
		addi %r5, %r6, 2579;\
		mulli %r6, %r5, 2304;\
		cmpw 7, %r5, %r4;\
		bne 7, label_wjojvyffcb;\
		mr %r4, %r6;\
	label_wjojvyffcb:\
		cmpwi 7, %r6, 937;\
		beq 7, label_rwppxpnenq;\
		mr %r1, %r5;\
	label_rwppxpnenq:\
		xori %r4, %r5, 3426;\
		rlwnm %r6, %r2, %r1, 1, 4;\
		srawi %r3, %r6, 7;\
	");
}
*/










/*
i386 output:
 EAX  0x10
 EBX  0x1c
 ECX  0x612c
 EDX  0x612c1fb0
 EDI  0xf042090
 ESI  0xffffffe4


x86_64 output:
 RAX  0x7800000000111484
 RBX  0xf
 RCX  0x0
 RDX  0x3ffffffffffef
 RDI  0x1e
 RSI  0x3fffffffff285

AArch64 output:
x1             0xfb05 843887f4      276001111705588
x2             0xfcff0000 06008307  -216454256989797625
x3             0x1f9 ff067e0c       2173237100044
x4             0xf9010000 0c7e06ff  -504121683079198977
x5             0x307e60ff 9f800000  3494337011894976512
x6             0xfcff 833f0600      278174348805632

mips output:
s1: 0x5f867ccc 
s2: 0x007978c2 
s3: 0x00000000 
s4: 0x00000000 
s5: 0x000005fa 
s6: 0x00000000

powerpc output:
r1             0xa13	2579
r2             0xffffff1f	4294967071
r3             0xf00000	15728640
r4             0x771	1905
r5             0xa13	2579
r6             0x78000000	2013265920
*/
