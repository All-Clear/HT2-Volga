import React from 'react'
import { Box, Grid, Button, Modal } from '@material-ui/core'
import Flippy, { FrontSide, BackSide } from 'react-flippy';

import first from "./static/first.png"
import second from "./static/second.png"
import third from "./static/third.png"
import fourth from "./static/fourth.png"


export default function Room({ room, handleBook }) {
    let passengers = [{ place_in_room: -1 }, { place_in_room: -1 }, { place_in_room: -1 }, { place_in_room: -1 }]
    room.tenants.forEach(item => {
        passengers[item.place_in_room-1] = item
    });
    console.log(room)
    return (
        <div>
            <Box sx={{ minHeight: 300, width: "85%", margin: "auto" }}>
                <Grid
                    container
                    direction="row"
                    justifyContent="center"
                    spacing={3}
                >
                    {passengers.map((pass, i) => {
                        return pass.place_in_room === -1 ? (
                            <Grid item md={3} key={i}>
                                <Flippy
                                    flipOnHover={true} // default false
                                    flipOnClick={false} // default false
                                    flipDirection="vertical"
                                    style={{ width: '100%', height: '300px' }} /// these are optional style, it is not necessary
                                >
                                    <FrontSide
                                        style={{
                                            backgroundColor: '#8a7788',
                                            color: "#fff"
                                        }}
                                    >
                                        <Box sx={{ height: "100%", width: "100%", alignItems: "center", display: "flex", justifyContent: "center", flexDirection: "column", textAlign: "center" }}>
                                            Свободно <br /> место - {i+1} домик - {room.address}
                                            {i === 0 ? <img src={first} alt="" style={{height: 200}} /> : ""}
                                            {i === 1 ? <img src={second} alt="" style={{ height: 200 }} /> : ""}
                                            {i === 2 ? <img src={third} alt="" style={{ height: 200 }} /> : ""}
                                            {i === 3 ? <img src={fourth} alt="" style={{ height: 200 }} /> : ""}
                                        </Box>
                                    </FrontSide>
                                    <BackSide
                                        style={{
                                            backgroundColor: '#8a7788',
                                            color: "#fff" }}>
                                        <Box sx={{ height: "100%", width: "100%", alignItems: "center", display: "flex", justifyContent: "center" }}>
                                            
                                            <Button onClick={() => handleBook(room.id_room, i + 1)} variant="contained" color="primary" disableElevation>
                                                Забронировать
                                            </Button>
                                        </Box>
                                    </BackSide>
                                </Flippy>
                            </Grid>
                        ) : (
                        <Grid item key={i} md={3}>
                            <Flippy
                                flipOnHover={true} // default false
                                flipOnClick={false} // default false
                                flipDirection="vertical"
                                style={{ width: '100%', height: '300px' }} /// these are optional style, it is not necessary
                            >
                                <FrontSide
                                    style={{
                                        backgroundColor: '#7B318F',
                                        color: "#fff"
                                    }}
                                >
                                    <Box sx={{ height: "100%", width: "100%", alignItems: "center", display: "flex", justifyContent: "center", flexDirection: "column" }}>
                                        Занятое место - {room.address} домик
                                        {i === 0 ? <img src={first} alt="" style={{ height: 200 }} /> : ""}
                                        {i === 1 ? <img src={second} alt="" style={{ height: 200 }} /> : ""}
                                        {i === 2 ? <img src={third} alt="" style={{ height: 200 }} /> : ""}
                                        {i === 3 ? <img src={fourth} alt="" style={{ height: 200 }} /> : ""}
                                    </Box>
                                </FrontSide>
                                <BackSide
                                            style={{ backgroundColor: '#7B318F', color: "#fff" }}>
                                    <ul style={{listStyle: "none", padding: 0}}>
                                        <li>{pass.gender ? "Мужчина" : "Женщина"} - {pass.age} лет</li>
                                        <li>{ pass.desire_communicate === null ? "Все равно на общение" :
                                        pass.desire_communicate ? "Хочет общаться" : "Не хочет общаться"}</li>
                                        {pass.hasChild ? <li>С маленьким ребенком</li> : ""}
                                        {pass.hasPet ? <li>С домашним животным</li> : ""}
                                        {pass.smoking ? <li>Курит</li> : ""}
                                        {pass.vaccination_against_covid19 ? <li>Вакцинирован от COVID-19</li> : ""}
                                        {pass.neighborsHasPet ? <li>Против домашних животных рядом</li> : ""}
                                        {pass.neighborsSmoking ? <li>Против курящих рядом</li> : ""}
                                        {pass.neighborsHasChild ? <li>Против маленьких детей рядом</li> : ""}
                                        {pass.interests.length === 0 ? "" : (
                                            <li>
                                                Интересы:
                                                <ul style={{ listStyle: "none" }}>
                                                    {pass.interests.map((item, i) => (
                                                        <li key={i}>{item}</li>
                                                    ))}
                                                </ul>
                                            </li>
                                        )}
                                    </ul>
                                </BackSide>
                            </Flippy>
                        </Grid>
                        )})}
                </Grid>
            </Box>
        </div>
    )
}
