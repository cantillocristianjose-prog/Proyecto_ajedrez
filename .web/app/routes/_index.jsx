import {Text as RadixThemesText} from "@radix-ui/themes"
import {Fragment,useEffect} from "react"
import {jsx} from "@emotion/react"





export default function Component() {





  return (
    jsx(Fragment,{},jsx(RadixThemesText,{as:"p"},"Hola reflex"),jsx("title",{}," | Index"),jsx("meta",{content:"favicon.ico",property:"og:image"},))
  )
}