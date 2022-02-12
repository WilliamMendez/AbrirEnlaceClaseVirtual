from webbrowser import open
import datetime

now = datetime.datetime.now()


def hacerHora(hora: int, min: int) -> datetime:
    return datetime.datetime(now.year, now.month, now.day, hora, min, 0, 0)


def buscarEnlace(hora, clasesDia: dict) -> str:
    # asdasd = input("esta verga se murió")
    enlace = "https://bloqueneon.uniandes.edu.co/d2l/home"
    for i in clasesDia.keys():
        diferencia = hora - i
        minutos = (diferencia.days * 24 * 60) + (diferencia.seconds/60)
        # print(i, hora, "\n", minutos)
        if ((-45 <= minutos) and (minutos <= 15)):
            enlace = clasesDia[i]

    return enlace


def abrirEnlace(enlace):
    open(enlace, 0, autoraise=True)
    # pass


clases = {0: {
            hacerHora(8, 00): "https://uniandes-edu-co.zoom.us/j/85308696080",
            hacerHora(12, 30): "https://teams.microsoft.com/l/channel/19%3aeFiG_UkPZ2edfnyKuhRdxAA699aB-1ueKxUTweMHXg01%40thread.tacv2/General?groupId=8f2b2738-52e5-4478-ac84-95baa20eba3a&tenantId=fabd047c-ff48-492a-8bbb-8f98b9fb9cca",
            hacerHora(16, 00): "https://nam10.safelinks.protection.outlook.com/?url=https%3A%2F%2Fteams.microsoft.com%2Fl%2Fteam%2F19%253a55DN38m1R1cIqdhaQgoubsm2BgwQ-eDuL3AaFGpgwrk1%2540thread.tacv2%2Fconversations%3FgroupId%3D1dbd0bb0-8a9c-4ccd-8977-8dca3f7a4743%26tenantId%3Dfabd047c-ff48-492a-8bbb-8f98b9fb9cca&amp;data=04%7C01%7Cw.mendez%40uniandes.edu.co%7C270b94792bc24c4c9ff308d959df9104%7Cfabd047cff48492a8bbb8f98b9fb9cca%7C0%7C0%7C637639639011333328%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C1000&amp;sdata=8KP7kRC4gRi%2FR7sU1%2BcWJY6K%2BbYUrGi8DhcQO169ITo%3D&amp;reserved=0",
            hacerHora(17, 00): "https://uniandes-edu-co.zoom.us/j/87286046281"
             },
          1: {
            hacerHora(8, 00): "https://teams.microsoft.com/_#/school/conversations/General?groupId=1dbd0bb0-8a9c-4ccd-8977-8dca3f7a4743&threadId=19:KTjpNfD09vPdzZ2EC2WPzhWosW2TMuiVYwp6wO3ncvE1@thread.tacv2&ctx=channel",
            hacerHora(11, 00): "https://uniandes-edu-co.zoom.us/j/96486781952?pwd=VXNSU3E2Uks5VEs3Y1FMeXgwVDNLUT09",
            hacerHora(17, 00): "https://uniandes-edu-co.zoom.us/j/81975958412"
             },
          2: {
            hacerHora(9, 30): "https://nam10.safelinks.protection.outlook.com/ap/t-59584e83/?url=https%3A%2F%2Fteams.microsoft.com%2Fl%2Fmeetup-join%2F19%253aQa1LUOYyzASOy5ljIP_DOSlLC5BZorJrne9fUxCHcSA1%2540thread.tacv2%2F1628627003143%3Fcontext%3D%257b%2522Tid%2522%253a%2522fabd047c-ff48-492a-8bbb-8f98b9fb9cca%2522%252c%2522Oid%2522%253a%2522222c5958-ab9b-4ae7-ad8b-e3600031e252%2522%257d&data=04%7C01%7Cw.mendez%40uniandes.edu.co%7Cfd61a23b2087411d107808d95c3fb38c%7Cfabd047cff48492a8bbb8f98b9fb9cca%7C0%7C0%7C637642251127111632%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C1000&sdata=F6QoUjL1n9sVRt3HHV0Kdslq8m4brV2eXSozHhRbLb8%3D&reserved=0",
            hacerHora(14, 00): "https://uniandes-edu-co.zoom.us/j/89537457894?pwd=T0dQNkdYV3M1Q0hOcWVBR1ZRYTRnUT09",
            hacerHora(17, 00): "https://uniandes-edu-co.zoom.us/j/87286046281"
             },
          3: {
            hacerHora(8, 00): "https://uniandes-edu-co.zoom.us/j/85308696080",
            hacerHora(11, 00): "https://uniandes-edu-co.zoom.us/j/96486781952?pwd=VXNSU3E2Uks5VEs3Y1FMeXgwVDNLUT09",
            hacerHora(12, 30): "https://bloqueneon.uniandes.edu.co/d2l/ext/rp/53614/lti/framedlaunch/a44d697c-b552-4a8c-b5e7-12fe6b8d704a",
            hacerHora(16, 00): "https://nam10.safelinks.protection.outlook.com/?url=https%3A%2F%2Fteams.microsoft.com%2Fl%2Fteam%2F19%253a55DN38m1R1cIqdhaQgoubsm2BgwQ-eDuL3AaFGpgwrk1%2540thread.tacv2%2Fconversations%3FgroupId%3D1dbd0bb0-8a9c-4ccd-8977-8dca3f7a4743%26tenantId%3Dfabd047c-ff48-492a-8bbb-8f98b9fb9cca&amp;data=04%7C01%7Cw.mendez%40uniandes.edu.co%7C270b94792bc24c4c9ff308d959df9104%7Cfabd047cff48492a8bbb8f98b9fb9cca%7C0%7C0%7C637639639011333328%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C1000&amp;sdata=8KP7kRC4gRi%2FR7sU1%2BcWJY6K%2BbYUrGi8DhcQO169ITo%3D&amp;reserved=0",
            hacerHora(17, 00): "https://uniandes-edu-co.zoom.us/j/81975958412"
             },
          4: {
            hacerHora(9, 30): "https://nam10.safelinks.protection.outlook.com/ap/t-59584e83/?url=https%3A%2F%2Fteams.microsoft.com%2Fl%2Fmeetup-join%2F19%253aQa1LUOYyzASOy5ljIP_DOSlLC5BZorJrne9fUxCHcSA1%2540thread.tacv2%2F1628627003143%3Fcontext%3D%257b%2522Tid%2522%253a%2522fabd047c-ff48-492a-8bbb-8f98b9fb9cca%2522%252c%2522Oid%2522%253a%2522222c5958-ab9b-4ae7-ad8b-e3600031e252%2522%257d&data=04%7C01%7Cw.mendez%40uniandes.edu.co%7Cfd61a23b2087411d107808d95c3fb38c%7Cfabd047cff48492a8bbb8f98b9fb9cca%7C0%7C0%7C637642251127111632%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C1000&sdata=F6QoUjL1n9sVRt3HHV0Kdslq8m4brV2eXSozHhRbLb8%3D&reserved=0",
            hacerHora(12, 30): "https://bloqueneon.uniandes.edu.co/d2l/ext/rp/53614/lti/framedlaunch/a44d697c-b552-4a8c-b5e7-12fe6b8d704a",
            hacerHora(14, 00): "https://uniandes-edu-co.zoom.us/j/89537457894?pwd=T0dQNkdYV3M1Q0hOcWVBR1ZRYTRnUT09",
            hacerHora(17, 00): "https://uniandes-edu-co.zoom.us/j/87286046281"
             }
         }


def main():
    dia = now.weekday()

    # print(now, dia)

    if dia < 5:
        clasesHoy = clases[dia]
    else:
        clasesHoy = {}

    link = buscarEnlace(now, clasesHoy)

    abrirEnlace(link)
    quit()
    # exit


main()
