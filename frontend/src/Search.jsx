import React, { useState } from "react"
import {
    Grid, FormControl, FormLabel,
    FormControlLabel, TextField, FormGroup,
    Select, Checkbox, MenuItem, Switch,
    InputLabel, Slider, Box, Typography, Button, CircularProgress,
    Snackbar, Container, Modal
} from "@material-ui/core"
import { Alert } from "@material-ui/lab"
import {
    MuiPickersUtilsProvider,
    KeyboardTimePicker,
    KeyboardDatePicker,
} from '@material-ui/pickers';
import Carousel from 'react-material-ui-carousel'
import Room from "./Room"
import style from "./style.css"
import DateFnsUtils from '@date-io/date-fns';
import { Redirect } from "react-router-dom"
import Registration from "./Registration"

const styleModal = {
    display: "flex",
    justifyContent: "center",
    position: 'absolute',
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    minWidth: 400,
    bgcolor: 'background.paper',
    boxShadow: 24,
    p: 4,
};

function ButtonComponent(props) {
    const { onClick, loading } = props;
    return (
        <Button color="primary" variant="outlined" onClick={onClick} disabled={loading}>
            {loading && <CircularProgress size={30} />}
            {!loading && 'Искать'}
        </Button>
    );
}

function valuetext(value) {
    return `${value}`;
}

export default () => {
    const [selectedDate, setSelectedDate] = React.useState(Date.now())
    const [selectedEndDate, setSelectedEndDate] = React.useState(Date.now())
    const [isLoading, setIsLoading] = useState(false)
    const [loading, setLoading] = useState(false)
    const [gender, setGender] = useState(1)
    const [age, setAge] = useState(18)
    const [communication, setCommunication] = useState(0)
    const [hasPet, setHasPet] = useState(false)
    const [hasGraft, setHasGraft] = useState(false)
    const [hasChild, setHasChild] = useState(false)
    const [isSmoking, setIsSmoking] = useState(false)
    const [preferences, setPreferences] = useState({
        "1": false,
        "2": false,
        "3": false,
        "4": false,
    })
    const { one, two, three, four } = preferences;
    const [neighborsAge, setNeighborsAge] = useState([20, 37])
    const [neighborsHasPet, setNeighborsHasPet] = useState(false)
    const [neighborsSmoking, setNeighborsSmoking] = useState(false)
    const [neighborsHasChild, setNeighborsHasChild] = useState(false)
    const [open, setOpen] = useState(false)

    const [openm, setOpenm] = useState(false);
    const handleOpenm = () => setOpenm(true);
    const handleClosem = () => setOpenm(false);

    const [scheme, setScheme] = useState(false);
    const openScheme = () => setScheme(true);
    const closeScheme = () => setScheme(false);

    const handleChangeGender = (event) => {
        setGender(event.target.value)
    }
    const handleChangeAge = (event) => {
        setAge(parseInt(event.target.value === "" ? 0 : event.target.value))
    }
    const handleChangeCommunication = (event) => {
        setCommunication(event.target.value)
    }
    const handleChangePet = (event) => {
        setHasPet(event.target.checked)
    }
    const handleChangeNeighborsPet = (event) => {
        setNeighborsHasPet(event.target.checked)
    }
    const handleChangeNeighborsSmoking = (event) => {
        setNeighborsSmoking(event.target.checked)
    }
    const handleChangeNeighborsChild = (event) => {
        setNeighborsHasChild(event.target.checked)
    }
    const handleChangeGraft = (event) => {
        setHasGraft(event.target.checked)
    }
    const handleChangeChild = (event) => {
        setHasChild(event.target.checked)
    }
    const handleChangeSmoking = (event) => {
        setIsSmoking(event.target.checked)
    }
    const handleChangePreferences = (event) => {
        setPreferences({
            ...preferences,
            [event.target.name]: event.target.checked,
        })
    }
    const handleChangeNeighborsAge = (event, newDataValue) => {
        setNeighborsAge(newDataValue)
    }
    const handleChangeList = (event) => {
        setChaisedList(event.target.checked)
    }
    const handleClose = (event, reason) => {
        if (reason === 'clickaway') {
            return;
        }

        setOpen(false);
    }

    const [id, setID] = useState("");
    const [place, setPlace] = useState(0);
    const book = () => {
        return async () => {
            setLoading(true)
            console.log("book")
            let user = {
                "date_start": selectedDate,
                "date_end": selectedEndDate,
                "id_room": id,
                "gender": gender,
                "age": age,
                "communication": communication,
                "hasPet": hasPet,
                "hasGraft": hasGraft,
                "hasChild": hasChild,
                "smoking": isSmoking,
                "preferences": {
                    "1": preferences['1'],
                    "2": preferences['2'],
                    "3": preferences['3'],
                    "4": preferences['4'],
                },
                "neighborsAge": neighborsAge,
                "neighborsHasPet": neighborsHasPet,
                "neighborsSmoking": neighborsSmoking,
                "neighborsHasChild": neighborsHasChild,
                "place_in_room": place
            }
            const res = await fetch('https://hip2.herokuapp.com/booking', {
                body: JSON.stringify(user),
                headers: {
                    'Content-Type': 'application/json'
                },
                method: 'POST',
            })
            console.log(id)
            setOpen(true)
            submit()
            handleClosem()
            setLoading(false)
        }
    }

    const handleBook = (id, place) => {
        setID(id)
        setPlace(place)
        console.log("booked")
        handleOpenm()
    }
    const handleDateChange = (date) => {
        setSelectedDate(date);
    };
    const handleEndDateChange = (date) => {
        setSelectedEndDate(date);
    };

    const [goodList, setGoodList] = useState([])
    const [alternativeList, setAlternativeList] = useState([])
    const [chaisedList, setChaisedList] = useState(false)

    const submit = async () => {
        setIsLoading(true)
        console.log('send')
        const body = {
            "gender": gender,
            "age": age,
            "communication": communication,
            "hasPet": hasPet,
            "hasGraft": hasGraft,
            "hasChild": hasChild,
            "smoking": isSmoking,
            "preferences": {
                "1": preferences['1'],
                "2": preferences['2'],
                "3": preferences['3'],
                "4": preferences['4'],
            },
            "neighborsAge": neighborsAge,
            "neighborsHasPet": neighborsHasPet,
            "neighborsSmoking": neighborsSmoking,
            "neighborsHasChild": neighborsHasChild,
        }
        console.log(body)
        const res = await fetch('https://hip2.herokuapp.com/sort', {
            body: JSON.stringify(body),
            headers: {
                'Content-Type': 'application/json'
            },
            method: 'POST',
        })
        let json = await res.json();
        console.log(json)
        console.log(json.good_list);
        setGoodList(json.good_list)
        setAlternativeList(json.alternative_list)
        setIsLoading(false)
    }
    return null;
}