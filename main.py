# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from caesar import CaesarCipher

if __name__ == '__main__':
    ciphercesar1 = CaesarCipher()
    ciphercesar2 = CaesarCipher()
    ciphercesar3 = CaesarCipher()

    ciphercesar1.set_plaintext("ABCDEFGHI")
    ciphercesar1.set_key(3)
    ciphercesar1.encrypt()
    print(ciphercesar1)

    ciphercesar2.set_ciphertext("Ymfy nx ymj vzjxynts")
    ciphercesar2.set_key(5)
    print(ciphercesar2)
    ciphercesar2.decrypt()
    print(ciphercesar2)

    ciphercesar3.set_ciphertext("Wr eh ru qrw wr eh")
    ciphercesar3.set_key(3)
    ciphercesar3.decrypt()
    print(ciphercesar3)

    ciphercesar4 = CaesarCipher()
    ciphercesar5 = CaesarCipher()
    ciphercesar6 = CaesarCipher()

    ciphercesar4.set_ciphertext("Lettc ria ciev")
    ciphercesar5.set_ciphertext("PhhwE dqnhq DP")
    ciphercesar6.set_ciphertext("xliasvphamhiaif")

    ciphercesar4.brute_decipher()
    ciphercesar5.brute_decipher()
    ciphercesar6.brute_decipher()

    """
    TP
    """

    ciphercesar7 = CaesarCipher()
    ciphercesar7.set_ciphertext(
        "NWLAHYCXPAJYQRNUNLQROOANVNWCYJAMNLJUJPNJDBBRLXWWDL" +
        "XVVNUNLQROOANMNLNBJAXDUNLXMNMNLNBJANBCDWNVNCQXMNMN" +
        "LQROOANVNWCCANBBRVYUNDCRURBNNYJASDUNBLNBJAMJWBBNBL" +
        "XAANBYXWMJWLNBBNLANCNB")
    ciphercesar8 = CaesarCipher()
    ciphercesar8.set_ciphertext(
        "vcfgrwqwfsbhfsntowbsobgfsbhfsnqvsnjcigsghqsoixcif" +
        "rviwtshseicwbsgojsnjcigdogeisjcigoihfsgofhwgobgjc" +
        "igbsrsjsnqwfqizsfrobgzsgfisgzsgxcifgcijfopzsgeioj" +
        "sqzsggwubsgrsjchfsdfctsggwcbdofzseiszsghhcbashwsf"
    )

    ciphercesar7.brute_decipher()
    ciphercesar8.brute_decipher()

    """
    solutions trouvées : clés 9 et 14
    """

    ciphercesar7.set_key(9)
    ciphercesar8.set_key(14)

    ciphercesar7.decrypt()
    ciphercesar8.decrypt()



    print(ciphercesar7)
    print(ciphercesar8)
