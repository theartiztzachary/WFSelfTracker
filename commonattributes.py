class Commonattributes:

    pages : dict
    polarities = ['Madurai', 'Vazarin', 'Naramon', 'Zenurik', 'Unairu', 'Penjaga', 'Umbra', 'Omni']
    warframe_identifiers = {
        # A
        'ash' : '/Lotus/Powersuits/Ninja/Ninja',
        'ash_prime' : '/Lotus/Powersuits/Ninja/AshPrime',
        'atlus' : '/Lotus/Powersuits/Brawler/Brawler',
        'atlus_prime' : 'uniqueName":"/Lotus/Powersuits/Brawler/AtlasPrime',
        # B
        'banshee' : '/Lotus/Powersuits/Banshee/Banshee',
        'banshee_prime' : '/Lotus/Powersuits/Banshee/BansheePrime',
        'baruuk' : '/Lotus/Powersuits/Pacifist/Pacifist',
        'baruuk_prime' : '/Lotus/Powersuits/Pacifist/BaruukPrime',
        # C
        'caliban' : '/Lotus/Powersuits/Sentient/Sentient',
        'caliban_prime' : 'none',
        'chroma' : '/Lotus/Powersuits/Dragon/Dragon',
        'chroma_prime' : '/Lotus/Powersuits/Dragon/ChromaPrime',
        'citrine' : '/Lotus/Powersuits/Geode/Geode',
        'citrine_prime' : 'none',
        'cyte_09_identifier' : '/Lotus/Powersuits/Frumentarius/Frumentarius',
        'cyte_09_prime' : 'none',
        # D
        'dagath' : '/Lotus/Powersuits/Dagath/Dagath',
        'dagath_prime' : 'none',
        'dante' : '/Lotus/Powersuits/Pagemaster/Pagemaster',
        'dante_prime' : 'none',
        # E
        'ember' : '/Lotus/Powersuits/Ember/Ember',
        'ember_prime' : '/Lotus/Powersuits/Ember/EmberPrime',
        'equinox' : '/Lotus/Powersuits/YinYang/YinYang',
        'equinox_prime' : '/Lotus/Powersuits/YinYang/EquinoxPrime',
        'excalibur' : '/Lotus/Powersuits/Excalibur/Excalibur',
        'excalibur_prime' : '/Lotus/Powersuits/Excalibur/ExcaliburPrime',
        'excalibur_umbra' : '/Lotus/Powersuits/Excalibur/ExcaliburUmbra',
        # F
        'frost' : '/Lotus/Powersuits/Frost/Frost',
        'frost_prime' : '/Lotus/Powersuits/Frost/FrostPrime',
        # G
        'gara' : '/Lotus/Powersuits/Glass/Glass',
        'gara_prime' : '/Lotus/Powersuits/Glass/GaraPrime',
        'garuda' : '/Lotus/Powersuits/Garuda/Garuda',
        'garuda_prime' : '/Lotus/Powersuits/Garuda/GarudaPrime',
        'gauss' : '/Lotus/Powersuits/Runner/Runner',
        'gauss_prime' : '/Lotus/Powersuits/Runner/GaussPrime',
        'grendel' : '/Lotus/Powersuits/Devourer/Devourer',
        'grendel_prime' : '/Lotus/Powersuits/Devourer/GrendelPrime',
        'gyre' : '/Lotus/Powersuits/Gyre/Gyre',
        'gyre_prime' : 'none',
        # H
        'harrow' : '/Lotus/Powersuits/Priest/Priest',
        'harrow_prime' : '/Lotus/Powersuits/Priest/HarrowPrime',
        'hildryn' : '/Lotus/Powersuits/IronFrame/IronFrame',
        'hildryn_prime' : '/Lotus/Powersuits/IronFrame/IronFramePrime',
        'hydroid' : '/Lotus/Powersuits/Pirate/Pirate',
        'hydroid_prime' : '/Lotus/Powersuits/Pirate/HydroidPrime',
        # I
        'inaros' : '/Lotus/Powersuits/Sandman/Sandman',
        'inaros_prime' : '/Lotus/Powersuits/Sandman/InarosPrime',
        'ivara' : '/Lotus/Powersuits/Ranger/Ranger',
        'ivara_prime' : '/Lotus/Powersuits/Ranger/IvaraPrime',
        # J
        'jade' : '/Lotus/Powersuits/Choir/Choir',
        'jade_prime' : 'none',
         # K
        'khora' : '/Lotus/Powersuits/Khora/Khora',
        'khora_prime' : '/Lotus/Powersuits/Khora/KhoraPrime',
        'koumei' : '/Lotus/Powersuits/Koumei/Koumei',
        'koumei_prime' : 'none',
        'kullervo' : '/Lotus/Powersuits/PaxDuviricus/PaxDuviricus',
        'kullervo_prime' : 'none',
        # L
        'lavos' : '/Lotus/Powersuits/Alchemist/Alchemist',
        'lavos_prime' : 'none', # soon tm
        'limbo' : '/Lotus/Powersuits/Magician/Magician',
        'limbo_prime' : '/Lotus/Powersuits/Magician/LimboPrime',
        'loki_identifier' : '/Lotus/Powersuits/Loki/Loki',
        'loki_prime' : '/Lotus/Powersuits/Loki/LokiPrime',
        # M
        'mag' : '/Lotus/Powersuits/Mag/Mag',
        'mag_prime' : '/Lotus/Powersuits/Mag/MagPrime',
        'mesa' : '/Lotus/Powersuits/Cowgirl/Cowgirl',
        'mesa_prime' : '/Lotus/Powersuits/Cowgirl/MesaPrime',
        'mirage' : '/Lotus/Powersuits/Harlequin/Harlequin',
        'mirage_prime' : '/Lotus/Powersuits/Harlequin/MiragePrime',
        # N
        'nekros' : '/Lotus/Powersuits/Necro/Necro',
        'nekros_prime' : '/Lotus/Powersuits/Necro/NekrosPrime',
        'nezha' : '/Lotus/Powersuits/Nezha/Nezha',
        'nezha_prime' : '/Lotus/Powersuits/Nezha/NezhaPrime',
        'nidus' : '/Lotus/Powersuits/Infestation/Infestation',
        'nidus_prime' : '/Lotus/Powersuits/Infestation/InfestationPrime',
        'nova' : '/Lotus/Powersuits/AntiMatter/Anti',
        'nova_prime' : '/Lotus/Powersuits/AntiMatter/NovaPrime',
        'nyx' : '/Lotus/Powersuits/Jade/Jade', #LMAO
        'nyx_prime' : '/Lotus/Powersuits/Jade/NyxPrime',
        # O
        'oberon' : '/Lotus/Powersuits/Paladin/Paladin',
        'oberon_prime' : '/Lotus/Powersuits/Paladin/PaladinPrime',
        'octavia' : '/Lotus/Powersuits/Bard/Bard',
        'octavia_prime_identifier' : '/Lotus/Powersuits/Bard/OctaviaPrime',
        # P
        'protea' : '/Lotus/Powersuits/Odalisk/Odalisk',
        'protea_prime' : '/Lotus/Powersuits/Odalisk/ProteaPrime',
        # Q
        'qorvex' : '/Lotus/Powersuits/ConcreteFrame/ConcreteFrame',
        'qorvex_prime' : 'none',
        # R
        'revenant' : '/Lotus/Powersuits/Revenant/Revenant',
        'revenant_prime_' : '/Lotus/Powersuits/Revenant/RevenantPrime',
        'rhino' : '/Lotus/Powersuits/Rhino/Rhino',
        'rhino_prime' : '/Lotus/Powersuits/Rhino/RhinoPrime',
        # S
        'saryn' : '/Lotus/Powersuits/Saryn/Saryn',
        'saryn_prime' : '/Lotus/Powersuits/Saryn/SarynPrime',
        'sevagoth' : '/Lotus/Powersuits/Wraith/Wraith',
        'sevagoth_prime' : '/Lotus/Powersuits/Wraith/SevagothPrime',
        'styanax' : '/Lotus/Powersuits/Hoplite/Hoplite',
        'styanax_prime' : 'none',
        # T
        'temple' : 'none', #soon tm
        'temple_prime' : 'none',
        'titania' : '/Lotus/Powersuits/Fairy/Fairy',
        'titania_prime' : '/Lotus/Powersuits/Fairy/TitaniaPrime',
        'trinity' : '/Lotus/Powersuits/Trinity/Trinity',
        'trinity_prime' : '/Lotus/Powersuits/Trinity/TrinityPrime',
        # U
        # V
        'valkyr' : '/Lotus/Powersuits/Berserker/Berserker',
        'valkyr_prime' : '/Lotus/Powersuits/Berserker/ValkyrPrime',
        'vauban' : '/Lotus/Powersuits/Trapper/Trapper',
        'vauban_prime' : '/Lotus/Powersuits/Trapper/TrapperPrime',
        'volt' : '/Lotus/Powersuits/Volt/Volt',
        'volt_prime' : '/Lotus/Powersuits/Volt/VoltPrime',
        'voruna' : '/Lotus/Powersuits/Werewolf/Werewolf',
        'voruna_prime' : 'none',
        # W
        'wisp' : '/Lotus/Powersuits/Wisp/Wisp',
        'wisp_prime' : '/Lotus/Powersuits/Wisp/WispPrime',
        'wukong' : '/Lotus/Powersuits/MonkeyKing/MonkeyKing',
        'wukong_prime' : '/Lotus/Powersuits/MonkeyKing/WukongPrime',
        # X
        'xaku' : '/Lotus/Powersuits/BrokenFrame/BrokenFrame',
        'xaku_prime' : '/Lotus/Powersuits/BrokenFrame/XakuPrime',
        # Y
        'yareli' : '/Lotus/Powersuits/Yareli/Yareli',
        'yareli_prime' : 'none',
        # Z
        'zephyr' : '/Lotus/Powersuits/Tengu/Tengu',
        'zephyr_prime' : '/Lotus/Powersuits/Tengu/ZephyrPrime'
     }

    ### NECHRAMECHS (these are under Warframes in the API!)

    # B
    bonewidow_identifier = '/Lotus/Powersuits/EntratiMech/ThanoTech'

    # V
    voidrig_identifier = '/Lotus/Powersuits/EntratiMech/NechroTech'

    ### nts - helminth abilities are also under warframes...i...guess...?


    def __init__(self):
        self.pages = {}