import { Controller, Get, Post, Body, Put, Param, Delete } from '@nestjs/common';
import { InventarioService } from './inventario.service';
import { CreateInventarioDto } from './dto/create-inventario.dto';
import { UpdateInventarioDto } from './dto/update-inventario.dto';
import { Inventario } from './Interface/inventario.interface';

@Controller('inventario')
export class InventarioController {
  constructor(private readonly inventarioService: InventarioService) {}

  @Post()
  async create(@Body() createInventarioDto: CreateInventarioDto): Promise<Inventario> {
    return this.inventarioService.create(createInventarioDto);
  }

  @Get()
  async findAll(): Promise<Inventario[]> {
    return this.inventarioService.findAll();
  }

  @Get(':id')
  async findOne(@Param('id') id: string): Promise<Inventario> {
    return this.inventarioService.findOne(id);
  }

  @Put(':id')
  async update(@Param('id') id: string, @Body() updateInventarioDto: UpdateInventarioDto): Promise<Inventario> {
    return this.inventarioService.update(id, updateInventarioDto);
  }

  @Delete(':id')
  async remove(@Param('id') id: string): Promise<Inventario> {
    return this.inventarioService.delete(id);
  }
}
