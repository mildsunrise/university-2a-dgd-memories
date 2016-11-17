-- 4x4 keypad analyzer for the DE2 board
-- clock frequency should be less than 500 Hz
-- version DD-2.1 - october 2015

library ieee;
use ieee.std_logic_1164.all;

entity keytest is
  port ( clk, nrst   : in  std_logic;
		nkey         : out std_logic;
		keycode, row : out std_logic_vector(3 downto 0);
		col          : in  std_logic_vector(3 downto 0) );
end keytest;

architecture arc_keytest of keytest is

  type states is (wait0, srow_all, crow_all, srow_1st, crow_1st, srow_2nd, crow_2nd,  
					srow_3rd, crow_3rd, srow_4th, crow_4th, wait1, checkit);
  signal FSM_state 			: states;
  signal count             	: integer range 0 to 15;
  signal look, kpressed 	: std_logic;

begin

--look generation from a mod 16 counter 
  process (clk, nrst)
  begin
    if nrst='0' then count <= 0;
    elsif clk'event and clk = '1' then 
		if FSM_state=wait0 or FSM_state=wait1 then count <= count + 1; end if;
    end if;
  end process;
  look <= '1' when count = 15 else '0';

--kpressed generation
  kpressed <= not (col(3) and col(2) and col(1) and col(0));

--whatkey FSM
--process describes state transitions  
--outputs described as concurrent assignments

  whatkey : process (clk, nrst)
  begin
    if nrst='0' then  FSM_state <= wait0;
    elsif clk'event and clk = '1' then
      case  FSM_state is
		when wait0 	=> if look='1' then  FSM_state <= srow_all; end if;
		when srow_all => FSM_state <= crow_all;
		when crow_all => if kpressed='1' then  FSM_state <= srow_1st; 
					   else FSM_state <= wait0; end if;
		when srow_1st => FSM_state <= crow_1st;
		when crow_1st => if kpressed='1' then  FSM_state <= wait1; 
					   else FSM_state <= srow_2nd; end if;
		when srow_2nd => FSM_state <= crow_2nd;
		when crow_2nd => if kpressed='1' then  FSM_state <= wait1; 
					   else FSM_state <= srow_3rd; end if;		
		when srow_3rd => FSM_state <= crow_3rd;
		when crow_3rd => if kpressed='1' then  FSM_state <= wait1; 
					   else FSM_state <= srow_4th; end if;
		when srow_4th => FSM_state <= crow_4th;
		when crow_4th => if kpressed='1' then  FSM_state <= wait1; 
					   else FSM_state <= wait0; end if;
		when wait1 	=> if look='1' then  FSM_state <= checkit; end if;
		when checkit => if kpressed='1' then  FSM_state <= wait1; 
					   else FSM_state <= wait0; end if;
	  end case;
    end if;
  end process whatkey;

  nkey <= '1' when (FSM_state = wait0 or FSM_state = srow_all or FSM_state = crow_all 
                   or FSM_state = wait1 or FSM_state = checkit or col = "1111") else '0';

  keycode <= x"1" when (FSM_state = crow_1st and col(0) = '0') else
             x"2" when (FSM_state = crow_1st and col(1) = '0') else
             x"3" when (FSM_state = crow_1st and col(2) = '0') else
             x"a" when (FSM_state = crow_1st and col(3) = '0') else
             x"4" when (FSM_state = crow_2nd and col(0) = '0') else
             x"5" when (FSM_state = crow_2nd and col(1) = '0') else
             x"6" when (FSM_state = crow_2nd and col(2) = '0') else
             x"b" when (FSM_state = crow_2nd and col(3) = '0') else
             x"7" when (FSM_state = crow_3rd and col(0) = '0') else
             x"8" when (FSM_state = crow_3rd and col(1) = '0') else
             x"9" when (FSM_state = crow_3rd and col(2) = '0') else
             x"c" when (FSM_state = crow_3rd and col(3) = '0') else
             x"e" when (FSM_state = crow_4th and col(0) = '0') else
             x"0" when (FSM_state = crow_4th and col(1) = '0') else
             x"f" when (FSM_state = crow_4th and col(2) = '0') else
             x"d" when (FSM_state = crow_4th and col(3) = '0') else
             x"0";

  with FSM_state select
     row <= "0000" when crow_all | checkit,
			"ZZZ0" when crow_1st,
			"ZZ0Z" when crow_2nd,
			"Z0ZZ" when crow_3rd,
			"0ZZZ" when crow_4th,
			"ZZZZ" when others;

end arc_keytest;
