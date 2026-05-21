package com.ccarolmaias.gamestore.Repository;

import org.springframework.data.repository.CrudRepository;

import com.ccarolmaias.gamestore.Model.Game;

public interface GameRepository extends CrudRepository<Game,Integer>{
    
}

