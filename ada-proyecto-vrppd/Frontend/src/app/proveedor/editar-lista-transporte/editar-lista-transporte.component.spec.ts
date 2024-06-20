import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EditarListaTransporteComponent } from './editar-lista-transporte.component';

describe('EditarListaTransporteComponent', () => {
  let component: EditarListaTransporteComponent;
  let fixture: ComponentFixture<EditarListaTransporteComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [EditarListaTransporteComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(EditarListaTransporteComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
