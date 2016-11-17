library ieee;
use ieee.std_logic_1164.all;

entity hex_disps is
  port ( sigA, sigB, sigRes : in std_logic;
         opA, opB : in std_logic_vector(3 downto 0);
         res : in std_logic_vector(7 downto 0);
         HEX7, HEX6, HEX5, HEX4, HEX3, HEX2, HEX1, HEX0 : out std_logic_vector (6 downto 0));
end;

architecture struct of hex_disps is
  component BCD7seg
    port ( num : in std_logic_vector (3 downto 0);
           HEX : out std_logic_vector (6 downto 0));
  end component;

  component CA2_SIG_SS
    port ( sig : in std_logic;
           ss : out std_logic_vector(6 downto 0));
  end component;
begin

  displaySigA: CA2_SIG_SS
    port map( sig => sigA, ss => HEX7 );
  displayA: BCD7seg
    port map( num => opA, HEX => HEX6 );

  displaySigB: CA2_SIG_SS
    port map( sig => sigB, ss => HEX5 );
  displayB: BCD7seg
    port map( num => opB, HEX => HEX4 );

  HEX3 <= "1111111";

  displaySigRes: CA2_SIG_SS
    port map( sig => sigRes, ss => HEX2 );
  displayRes1: BCD7seg
    port map( num => res(7 downto 4), HEX => HEX1 );
  displayRes0: BCD7seg
    port map( num => res(3 downto 0), HEX => HEX0 );

end struct;
