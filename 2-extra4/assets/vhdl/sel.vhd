library ieee;
use ieee.std_logic_1164.all;

entity sel is
  port ( sig : in std_logic;
         res : in std_logic_vector(7 downto 0);
         show : in std_logic;
         selSig : out std_logic;
         sel : out std_logic_vector(7 downto 0) );
end;

architecture logic of sel is
begin
  selSig <= sig when show = '1' else '0';
  sel <= res when show = '1' else "11111111";
end logic;
