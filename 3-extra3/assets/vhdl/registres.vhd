library ieee;
use ieee.std_logic_1164.all;

entity registres is
  port ( clk : in std_logic;
         nrst : in std_logic;
         eshft : in std_logic;
         keycode : in std_logic_vector(3 downto 0);
         num : out std_logic_vector(11 downto 0) );
end;

architecture logic of registres is
  signal a, b, c : std_logic_vector(3 downto 0);
begin
  process (clk,nrst)
  begin
  if nrst = '0' then
    a <= "0000";
    b <= "0000";
    c <= "0000";
  elsif rising_edge(clk) then
    if eshft = '1' then
      c <= b;
      b <= a;
      a <= keycode;
    end if;
  end if;
  end process;
  
  num <= c & b & a;
end logic;
