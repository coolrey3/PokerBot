from poker import Range

# GTO Opening Ranges
class PositionRange:
    sbOpen = Range(
        'AA-22 AKs-A2s KQs-K2s QJs-Q4s JTs-J7s T9s-T7s 98s-97s 87s-86s 76s-75s 65s-64s 54s AKo-A7o KQo-K9o QJo-Q9o JTo-J9o T9o 98o')

    utgOpen = Range('AA-33 AKo-AJo KQo AKs-ATs KQs-KTs QJs-QTs JTs-J9s T9s 98s 87s 76s 65s')

    mpOpen = Range('AA-22 AKs-A7s A5s KQs-KTs QJs-QTs JTs-J9s T9s-T8s 98s-97s 87s-86s 76s-75s 65s 54s AKo-ATo KQo')

    coOpen = Range(
        'AA-22 AKs-A2s KQs-K6s QJs-Q7s JTs-J8s T9s-T8s 98s-97s 87s-86s 76s-75s 65s-64s 54s AKo-ATo KQo-KJo QJo')

    buttonOpen = Range(
        'AA-22 AKs-A2s KQs-K2s QJs-Q2s JTs-J5s T9s-T6s 98s-96s 87s-85s 76s-74s 65s-64s 54s-53s 43s AKo-A2o KQo-K7o QJo-Q9o JTo-J9o T9o-T8o 98o 87o')

    sbRaiseIn = Range('AA')
    utgRaiseIn = Range('AA 88')
    mpRaiseIn = Range('AA')
    btnRaiseIn = Range('AA')
    coRaiseIn = Range('AA')