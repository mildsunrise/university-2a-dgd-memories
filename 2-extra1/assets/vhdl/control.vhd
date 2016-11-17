library ieee;
use ieee.std_logic_1164.all;

entity control is
  port( clk, nrst, bcd, neg, ast, coi : in std_logic;
		intro, negar, show : out std_logic );
end control;

architecture arq of control is
  type machine is ( st_show, st_intro );
  signal state : machine;
begin
  process(clk, nrst) 
  begin
	if nrst='0' then state <= st_show;
	elsif (clk'event and clk='1') then
		case state is
			when st_show  => if ast='1' then state <= st_intro; end if;
			when st_intro => if coi='1' then state <= st_show; end if;
		end case;
	end if;
end process;

intro <= '1' when state=st_intro and bcd='1' else '0';
negar <= '1' when state=st_intro and neg='1' else '0';
show  <= '1' when state=st_show else '0';

end arq;
