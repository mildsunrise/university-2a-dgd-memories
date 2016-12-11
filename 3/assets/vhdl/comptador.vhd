library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity comptador is
  port ( ecnt : in std_logic;
         nrst, clk : in std_logic;
         numx : out std_logic_vector(7 downto 0) );
end;

architecture logic of comptador is
  signal n1 : unsigned(3 downto 0);
  signal n0 : unsigned(3 downto 0);
begin
  process (clk, nrst)
  begin
    if nrst = '0' then
      n1 <= x"0";
      n0 <= x"0";
    elsif (clk'event and clk = '1') then

      if ecnt = '1' then
        if n0 = 9 then
          if n1 = 9 then n1 <= x"0"; else n1 <= n1 + 1; end if;
          n0 <= x"0";
        else
          n0 <= n0 + 1;
        end if;
      end if;

    end if;
  end process;

  numx <= std_logic_vector(n1) & std_logic_vector(n0);
end logic;
