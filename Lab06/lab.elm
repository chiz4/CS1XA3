module Main exposing (main)

import Browser
import Html exposing (..)
import Html.Attributes exposing (..)
import Html.Events exposing (..)

main = 
       Browser.sandbox { init = init, update = update, view = view }

type alias Model =
        { first : String
        , second : String
        }

init : Model
init =
        Model "" ""

type Msg
        = First String
        | Second String

update : Msg -> Model -> Model
update msg model =
        case msg of
                First first ->
                        { model | first = first }
                Second second ->
                        { model | second = second }

view : Model -> Html Msg
view model =
        div []
                [ input [ type_ "text", value model.first, onInput First ] []
                , input [ type_ "text", value model.second, onInput Second ] []
                , div [] [ text (model.first), text ":", text (model.second) ]
                ]
