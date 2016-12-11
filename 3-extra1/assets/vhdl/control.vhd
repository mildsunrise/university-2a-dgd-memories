library ieee;
use ieee.std_logic_1164.all;

entity control is
  port ( bcd, ast, coi : in std_logic;
         ngtx, neqx, nltx : in std_logic;
         clk, nrst : in std_logic;
         eshft, ecnt : out std_logic;
         comp : out std_logic_vector(2 downto 0) );
end control;

architecture arq of control is
  type machine is ( st_idle, st_playing );
  signal state : machine;
begin
  process(clk, nrst)
  begin
    if nrst='0' then
      state <= st_idle;
      comp <= "111";
    elsif (clk'event and clk='1') then
      case state is
        when st_idle =>
          if coi='1' then state <= st_playing; comp <= "000"; end if;
        when st_playing =>
          if coi = '1' then state <= st_idle; comp <= "111"; end if;
          if ast = '1' and neqx = '1' then state <= st_idle; end if;
          if ast = '1' then comp <= nltx & neqx & ngtx; end if;
          if bcd = '1' then comp <= "000"; end if;
      end case;
    end if;
  end process;

  ecnt <= '1' when state = st_idle else '0';
  eshft <= '1' when (state = st_playing and bcd = '1') else '0';
end arq;

