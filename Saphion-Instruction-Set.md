cat <<'EOF' > Burtons-Toy--axiomatic-computation-system--The-Saphion.md
The Saphion Instruction Set
==

The Saphion is a 2 space processor, where the spaces can take values
of 1 and 0. These 'spaces' are called 'e' and 'a'.

--

#
# The Essentials
#
00 tri - put at random 0 or 1 in space 'e', reset with meta.
         'tri' only works once until reset with meta;
         calling again gives the same value.

01 not - invert the value of space 'e', from 0 to 1 and 1 to 0.

02 swap - swap the contents of space 'e' and 'a'. 
	      Write 'e' (now 'a') to tape.

03 mov - copy the contents of space 'a' to space 'e', overwriting 'e'.

## Optional

##04 and - space 'e' & (and) space 'a' into space 'e'

##05 or - space 'e' | (or) space 'a' into space 'e'

#
# The Stack -- 'For fun'
#

04 push - prepend 'e' into a 'stack' space

05 pop - pop from the 'stack' space into 'e'

06 rotate - rotate the 'stack' space, downward from 1 to 0, from 
	        beginning to end.
#
# The Directions -- 'Comms'
#

07 up - swap 'e' and the 'up' space

08 down - swap 'e' and the 'down' space

09 left - swap 'e' and the 'left' space

10 right - swap 'e' and the 'right' space

11 in - swap 'e' and the 'in' space

12 out - swap 'e' and the 'out' space

##12 xor - space 'e' ^ (xor) space 'a' into space 'e'

##12 or - it made a comeback

13 meta - Code or Comment. Resets the Saphion, so you can use tri again.

# For example:
#

meta pushe is push which prepends 'e' into the 'stack' space

meta pusha is swap push swap which prepends 'a' into the 'stack' space

meta trie is tri which places a random bit in the 'e' space

meta tria is tri swap which places a random bit in the 'a' space, destroying the 'e' space

meta note is not which inverts 'e', from 0 to 1 or from 1 to 0

meta nota is swap not swap which which inverts 'a', from 0 to 1 or from 1 to 0

meta ande is and which puts 'e' & 'a' into 'e'

meta anda is and swap which destroys 'e' and replaces it with 'a', puts 'e' & 'a' into 'a'

meta ore is or which puts 'e' | 'a' into 'e'

meta ora is or swap which destroys 'e' or replaces it with 'a', puts 'e' | 'a' into 'a'

meta xore is xor which puts 'e' | 'a' into 'e'

meta xora is xor swap which destroys 'e' xor replaces it with 'a', puts 'e' | 'a' into 'a'

meta nore is nor which puts 'e' | 'a' into 'e'

meta nora is nor swap which destroys 'e' nor replaces it with 'a', puts 'e' | 'a' into 'a'
#
meta ine is in which swaps the contents of 'e' with the 'in' space

meta ina is in swap which swaps the contents of 'a' into the 'in' space, destroying the 'e' space

meta oute is out which swaps the contents of 'e' with the 'out' space

meta outa is swap out swap which swaps the contents of 'a' with the 'out' space

meta lefte is left which swaps the contents of 'e' with the 'left' space

meta lefta is swap left swap which swaps the contents of 'a' with the 'left' space1

meta righte is right which swaps the contents of 'e' with the 'right' space

meta righta is swap right swap which swaps the contents of 'a' with the 'right' space

meta ine is in which swaps the contents of 'e' with the 'in' space

meta ina is swap in swap which swaps the contents of 'a' with the 'in' space

meta oute is out which swaps the contents of 'e' with the 'out' space

meta outa is swap out swap which swaps the contents of 'a' with the 'out' space
#
meta equal is and which compares the two spaces and puts 1 in 'e' if they are the same

meta not-equal is equal note which compares the two spaces and puts 1 in 'e' 

# meta greater-than is ...

14 nor - the universal instruction

15 clear - set space 'e' to 0

EOF

--
Burton John Samograd
burtonjohnsamograd@protonmail.com
2023
